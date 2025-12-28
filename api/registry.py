"""
Central registry for all prompt adapters.
Maps model names to their corresponding adapter instances.
"""

from adapters.image import (
    DalleAdapter,
    MidjourneyAdapter,
    StableDiffusionAdapter,
    ImagenAdapter,
    FireflyAdapter,
)
from adapters.video import (
    SoraAdapter,
    RunwayAdapter,
    PikaAdapter,
    VeoAdapter,
    StableVideoDiffusionAdapter,
)
from adapters.audio import (
    OpenAIAudioAdapter,
    ElevenLabsAdapter,
    SeamlessM4TAdapter,
    IndicTTSAdapter,
    CoquiTTSAdapter,
)
from adapters.text import (
    GPT4Adapter,
    LlamaAdapter,
    MistralAdapter,
    GeminiAdapter,
    ClaudeAdapter,
)

# Registry mapping model names to adapter instances
ADAPTER_REGISTRY = {
    # Text/LLM models
    "gpt-4": GPT4Adapter(),
    "llama-3": LlamaAdapter(),
    "mistral": MistralAdapter(),
    "gemini": GeminiAdapter(),
    "claude": ClaudeAdapter(),
    # Image models
    "dalle": DalleAdapter(),
    "stable-diffusion": StableDiffusionAdapter(),
    "midjourney": MidjourneyAdapter(),
    "imagen": ImagenAdapter(),
    "firefly": FireflyAdapter(),
    # Video models
    "sora": SoraAdapter(),
    "runway": RunwayAdapter(),
    "pika": PikaAdapter(),
    "veo": VeoAdapter(),
    "stable-video-diffusion": StableVideoDiffusionAdapter(),
    # Audio models
    "openai-audio": OpenAIAudioAdapter(),
    "elevenlabs": ElevenLabsAdapter(),
    "seamless-m4t": SeamlessM4TAdapter(),
    "indic-tts": IndicTTSAdapter(),
    "coqui-tts": CoquiTTSAdapter(),
}


def get_available_models_by_modality():
    """Return available models grouped by modality."""
    return {
        "text": ["gpt-4", "llama-3", "mistral", "gemini", "claude"],
        "image": ["dalle", "stable-diffusion", "midjourney", "imagen", "firefly"],
        "video": ["sora", "runway", "pika", "veo", "stable-video-diffusion"],
        "audio": ["openai-audio", "elevenlabs", "seamless-m4t", "indic-tts", "coqui-tts"],
    }
