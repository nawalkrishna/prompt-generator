"""
Unit tests for prompt adapters.
"""

import pytest
from schema import ImagePrompt, VideoPrompt, VoicePrompt
from adapters.image import (
    DalleAdapter,
    MidjourneyAdapter,
    StableDiffusionAdapter,
    ImagenAdapter,
    FireflyAdapter,
)
from adapters.video import RunwayAdapter, PikaAdapter, SoraAdapter
from adapters.voice import OpenAIVoiceAdapter, ElevenLabsAdapter


class TestImageAdapters:
    """Tests for image generation adapters."""

    def test_dalle_adapter_basic(self):
        adapter = DalleAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a cat",
            style="photorealistic",
        )
        result = adapter.compile(prompt)

        assert "cat" in result
        assert "photorealistic" in result
        assert isinstance(result, str)

    def test_dalle_adapter_with_optional_fields(self):
        adapter = DalleAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a cat",
            style="photorealistic",
            environment="garden",
            lighting="golden hour",
            mood="peaceful",
        )
        result = adapter.compile(prompt)

        assert "garden" in result
        assert "golden hour" in result
        assert "peaceful" in result

    def test_midjourney_adapter(self):
        adapter = MidjourneyAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a dragon",
            style="fantasy art",
            aspect_ratio="16:9",
        )
        result = adapter.compile(prompt)

        assert "dragon" in result
        assert "--ar 16:9" in result
        assert "--v 6" in result
        assert "--q 2" in result

    def test_midjourney_adapter_default_aspect_ratio(self):
        adapter = MidjourneyAdapter()
        prompt = ImagePrompt(
            modality="image", goal="test", subject="a landscape", style="painting"
        )
        result = adapter.compile(prompt)

        assert "--ar 16:9" in result  # default

    def test_sdxl_adapter(self):
        adapter = StableDiffusionAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a robot",
            style="sci-fi",
            negative_constraints=["blurry", "low quality"],
        )
        result = adapter.compile(prompt)

        assert "Positive:" in result
        assert "Negative:" in result
        assert "robot" in result
        assert "blurry" in result

    def test_imagen_adapter(self):
        adapter = ImagenAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a person",
            environment="office",
        )
        result = adapter.compile(prompt)

        assert "person" in result
        assert "office" in result
        assert "realistic" in result.lower()

    def test_firefly_adapter(self):
        adapter = FireflyAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a product",
            style="minimalist",
        )
        result = adapter.compile(prompt)

        assert "product" in result
        assert "professional" in result.lower() or "commercial" in result.lower()


class TestVideoAdapters:
    """Tests for video generation adapters."""

    def test_runway_adapter(self):
        adapter = RunwayAdapter()
        prompt = VideoPrompt(
            modality="video",
            goal="test",
            subject="test",
            scene="city street",
            action="people walking",
            camera_motion="tracking shot",
            duration_seconds=10,
        )
        result = adapter.compile(prompt)

        assert "city street" in result
        assert "people walking" in result
        assert "tracking shot" in result
        assert "10-second" in result

    def test_pika_adapter(self):
        adapter = PikaAdapter()
        prompt = VideoPrompt(
            modality="video",
            goal="test",
            subject="test",
            scene="forest",
            action="bird flying",
            duration_seconds=5,
        )
        result = adapter.compile(prompt)

        assert "Scene:" in result
        assert "forest" in result
        assert "Action:" in result
        assert "bird flying" in result
        assert "5s" in result

    def test_sora_adapter(self):
        adapter = SoraAdapter()
        prompt = VideoPrompt(
            modality="video",
            goal="test",
            subject="test",
            scene="beach at sunset",
            action="waves crashing",
            camera_motion="slow pan",
            duration_seconds=15,
        )
        result = adapter.compile(prompt)

        assert "beach at sunset" in result
        assert "waves crashing" in result
        assert "slow pan" in result
        assert "15-second" in result


class TestVoiceAdapters:
    """Tests for voice synthesis adapters."""

    def test_openai_voice_adapter(self):
        adapter = OpenAIVoiceAdapter()
        prompt = VoicePrompt(
            modality="voice",
            goal="test",
            subject="test",
            accent="American",
            emotion="calm",
            pace="medium",
        )
        result = adapter.compile(prompt)

        assert "American" in result
        assert "calm" in result
        assert "medium" in result

    def test_elevenlabs_adapter(self):
        adapter = ElevenLabsAdapter()
        prompt = VoicePrompt(
            modality="voice",
            goal="test",
            subject="test",
            voice_gender="female",
            accent="British",
            emotion="excited",
            pace="fast",
        )
        result = adapter.compile(prompt)

        assert "Voice: female" in result
        assert "Accent: British" in result
        assert "Emotion: excited" in result
        assert "Pace: fast" in result
        assert "Stability:" in result
        assert "Clarity:" in result


class TestAdapterEdgeCases:
    """Tests for edge cases and error handling."""

    def test_minimal_image_prompt(self):
        adapter = DalleAdapter()
        prompt = ImagePrompt(modality="image", goal="test", subject="a dog")
        result = adapter.compile(prompt)

        assert "dog" in result
        assert isinstance(result, str)
        assert len(result) > 0

    def test_prompt_with_none_values(self):
        adapter = MidjourneyAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a cat",
            lighting=None,
            mood=None,
        )
        result = adapter.compile(prompt)

        # Should not include "None" in output
        assert "None" not in result

    def test_empty_negative_constraints(self):
        adapter = StableDiffusionAdapter()
        prompt = ImagePrompt(
            modality="image",
            goal="test",
            subject="a tree",
            negative_constraints=[],
        )
        result = adapter.compile(prompt)

        assert "tree" in result
        # Should have default negative constraints
        assert "Negative:" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
