import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from compiler import PromptCompiler
from schema import ImagePrompt, VideoPrompt, VoicePrompt, TextPrompt
from registry import get_available_models_by_modality
from rate_limiter import rate_limit, sanitize_payload

app = Flask(__name__)
CORS(app)

compiler = PromptCompiler()

# Input validation limits
MAX_TEXT_LENGTH = 2000
MAX_DURATION_SECONDS = 60


def validate_request_data(data):
    """Validate incoming request data."""
    if not data:
        return "Request body is required", 400

    modality = data.get("modality")
    model = data.get("model")
    payload = data.get("payload")

    if not modality:
        return "Missing required field: modality", 400

    if modality not in ["text", "image", "video", "audio"]:
        return f"Invalid modality: {modality}. Must be one of: text, image, video, audio", 400

    if not model:
        return "Missing required field: model", 400

    available_models = get_available_models_by_modality()
    if model not in available_models.get(modality, []):
        return (
            f"Invalid model '{model}' for modality '{modality}'. "
            f"Available models: {', '.join(available_models[modality])}",
            400,
        )

    if not payload:
        return "Missing required field: payload", 400

    if not isinstance(payload, dict):
        return "Payload must be a dictionary", 400

    # Validate text field lengths
    for key, value in payload.items():
        if isinstance(value, str) and len(value) > MAX_TEXT_LENGTH:
            return f"Field '{key}' exceeds maximum length of {MAX_TEXT_LENGTH}", 400

    # Validate duration for video
    if modality == "video" and "duration_seconds" in payload:
        duration = payload.get("duration_seconds")
        try:
            duration = int(duration)
            if duration < 1 or duration > MAX_DURATION_SECONDS:
                return (
                    f"duration_seconds must be between 1 and {MAX_DURATION_SECONDS}",
                    400,
                )
        except (ValueError, TypeError):
            return "duration_seconds must be a valid integer", 400

    return None


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})


@app.route("/api/models", methods=["GET"])
def get_models():
    """Get available models grouped by modality."""
    try:
        models = get_available_models_by_modality()
        return jsonify({"models": models})
    except Exception as e:
        return jsonify({"error": "Failed to fetch models"}), 500


@app.route("/api/generate", methods=["POST"])
def generate_prompt():
    """Generate optimized prompt for specified model."""
    try:
        data = request.json

        # Validate request
        validation_error = validate_request_data(data)
        if validation_error:
            error_msg, status_code = validation_error
            return jsonify({"error": error_msg}), status_code

        modality = data["modality"]
        model = data["model"]
        payload = data["payload"]

        # Sanitize payload to prevent injection
        payload = sanitize_payload(payload, MAX_TEXT_LENGTH)

        # Create appropriate prompt object
        try:
            if modality == "text":
                prompt = TextPrompt(**payload)
            elif modality == "image":
                prompt = ImagePrompt(**payload)
            elif modality == "video":
                prompt = VideoPrompt(**payload)
            elif modality == "audio":
                prompt = VoicePrompt(**payload)
        except TypeError as e:
            return jsonify({"error": f"Invalid payload: {str(e)}"}), 400

        # Compile prompt
        result = compiler.compile(prompt, model)

        return jsonify({"prompt": result, "model": model, "modality": modality})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


# For Vercel serverless function
def handler(request):
    with app.request_context(request.environ):
        return app.full_dispatch_request()
