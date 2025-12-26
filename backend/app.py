import os
import logging
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from compiler import PromptCompiler
from schema import ImagePrompt, VideoPrompt, VoicePrompt, TextPrompt
from registry import get_available_models_by_modality
from rate_limiter import rate_limit, sanitize_payload

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("prompt_generator.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure CORS - restrict in production
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
CORS(app, origins=allowed_origins)

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


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})


@app.route("/models", methods=["GET"])
def get_models():
    """Get available models grouped by modality."""
    try:
        models = get_available_models_by_modality()
        return jsonify({"models": models})
    except Exception as e:
        logger.error(f"Error fetching models: {str(e)}")
        return jsonify({"error": "Failed to fetch models"}), 500


@app.route("/generate", methods=["POST"])
@rate_limit(max_requests=int(os.getenv("RATE_LIMIT", 60)), window_seconds=60)
def generate_prompt():
    """Generate optimized prompt for specified model."""
    try:
        data = request.json

        # Validate request
        validation_error = validate_request_data(data)
        if validation_error:
            error_msg, status_code = validation_error
            logger.warning(f"Validation error: {error_msg}")
            return jsonify({"error": error_msg}), status_code

        modality = data["modality"]
        model = data["model"]
        payload = data["payload"]

        # Sanitize payload to prevent injection
        payload = sanitize_payload(payload, MAX_TEXT_LENGTH)

        logger.info(f"Generating prompt for modality={modality}, model={model}")

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
            logger.error(f"Invalid payload structure: {str(e)}")
            return jsonify({"error": f"Invalid payload: {str(e)}"}), 400

        # Compile prompt
        result = compiler.compile(prompt, model)

        logger.info(f"Successfully generated prompt for {model}")
        return jsonify({"prompt": result, "model": model, "modality": modality})

    except ValueError as e:
        logger.error(f"Value error: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    """Handle 405 errors."""
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    logger.info(f"Starting Flask server on {host}:{port}")
    app.run(host=host, port=port, debug=debug, use_reloader=False)

