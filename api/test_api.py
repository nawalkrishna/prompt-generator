"""
Integration tests for Flask API.
"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_check(self, client):
        response = client.get("/health")
        assert response.status_code == 200

        data = json.loads(response.data)
        assert data["status"] == "healthy"
        assert "timestamp" in data


class TestModelsEndpoint:
    """Tests for the models endpoint."""

    def test_get_models(self, client):
        response = client.get("/models")
        assert response.status_code == 200

        data = json.loads(response.data)
        assert "models" in data
        assert "image" in data["models"]
        assert "video" in data["models"]
        assert "voice" in data["models"]

        # Check specific models
        assert "dalle-3" in data["models"]["image"]
        assert "runway-gen3" in data["models"]["video"]
        assert "openai-voice" in data["models"]["voice"]


class TestGenerateEndpoint:
    """Tests for the prompt generation endpoint."""

    def test_generate_image_prompt_dalle(self, client):
        payload = {
            "modality": "image",
            "model": "dalle-3",
            "payload": {
                "modality": "image",
                "goal": "test",
                "subject": "a cat",
                "style": "photorealistic",
            },
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert "prompt" in data
        assert "cat" in data["prompt"]

    def test_generate_video_prompt_sora(self, client):
        payload = {
            "modality": "video",
            "model": "sora",
            "payload": {
                "modality": "video",
                "goal": "test",
                "subject": "test",
                "scene": "city street",
                "action": "people walking",
                "duration_seconds": 10,
            },
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert "prompt" in data
        assert "city street" in data["prompt"]

    def test_generate_voice_prompt_elevenlabs(self, client):
        payload = {
            "modality": "voice",
            "model": "elevenlabs",
            "payload": {
                "modality": "voice",
                "goal": "test",
                "subject": "test",
                "accent": "American",
                "emotion": "calm",
                "pace": "medium",
            },
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 200
        data = json.loads(response.data)
        assert "prompt" in data

    def test_missing_modality(self, client):
        payload = {
            "model": "dalle-3",
            "payload": {"subject": "a cat"},
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_invalid_modality(self, client):
        payload = {
            "modality": "invalid",
            "model": "dalle-3",
            "payload": {"subject": "a cat"},
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data
        assert "modality" in data["error"].lower()

    def test_missing_model(self, client):
        payload = {
            "modality": "image",
            "payload": {"subject": "a cat"},
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_invalid_model(self, client):
        payload = {
            "modality": "image",
            "model": "invalid-model",
            "payload": {"subject": "a cat"},
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_missing_payload(self, client):
        payload = {
            "modality": "image",
            "model": "dalle-3",
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_empty_request_body(self, client):
        response = client.post(
            "/generate", data=json.dumps({}), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data

    def test_text_field_too_long(self, client):
        payload = {
            "modality": "image",
            "model": "dalle-3",
            "payload": {
                "modality": "image",
                "goal": "test",
                "subject": "a" * 3000,  # Exceeds MAX_TEXT_LENGTH
                "style": "photorealistic",
            },
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data
        assert "length" in data["error"].lower()

    def test_invalid_duration(self, client):
        payload = {
            "modality": "video",
            "model": "sora",
            "payload": {
                "modality": "video",
                "goal": "test",
                "subject": "test",
                "scene": "city",
                "action": "walking",
                "duration_seconds": 1000,  # Too long
            },
        }

        response = client.post(
            "/generate", data=json.dumps(payload), content_type="application/json"
        )

        assert response.status_code == 400
        data = json.loads(response.data)
        assert "error" in data


class TestErrorHandlers:
    """Tests for error handlers."""

    def test_404_error(self, client):
        response = client.get("/nonexistent")
        assert response.status_code == 404

        data = json.loads(response.data)
        assert "error" in data

    def test_405_error(self, client):
        response = client.get("/generate")  # Should be POST
        assert response.status_code == 405

        data = json.loads(response.data)
        assert "error" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
