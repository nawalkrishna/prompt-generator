/**
 * Central configuration for the Prompt Generator application.
 * Single source of truth for models, validation rules, and API settings.
 */

// API Configuration
export const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

// Available models by modality
export const MODELS = {
  text: [
    { value: "gpt-4", label: "GPT-4 / GPT-4.1 / GPT-4o", description: "OpenAI's most capable model" },
    { value: "llama-3", label: "Meta LLaMA 3", description: "Open-source powerhouse" },
    { value: "mistral", label: "Mistral / Mixtral", description: "Efficient European AI" },
    { value: "gemini", label: "Google Gemini", description: "Multimodal intelligence" },
    { value: "claude", label: "Anthropic Claude", description: "Advanced reasoning and analysis" },
  ],
  image: [
    { value: "dalle", label: "DALL·E", description: "OpenAI's image generator" },
    { value: "stable-diffusion", label: "Stable Diffusion", description: "Open-source, customizable" },
    { value: "midjourney", label: "Midjourney", description: "High-quality artistic images" },
    { value: "imagen", label: "Google Imagen", description: "Photorealistic generations" },
    { value: "firefly", label: "Adobe Firefly", description: "Commercial-safe content" },
  ],
  video: [
    { value: "sora", label: "OpenAI Sora", description: "Advanced coherent videos" },
    { value: "runway", label: "Runway Gen-2 / Gen-3", description: "Cinematic video generation" },
    { value: "pika", label: "Pika Labs Pika", description: "Easy-to-use video creator" },
    { value: "veo", label: "Google Veo", description: "High-quality video generation" },
    { value: "stable-video-diffusion", label: "Stable Video Diffusion", description: "Open-source video AI" },
  ],
  audio: [
    { value: "openai-audio", label: "OpenAI Whisper + TTS", description: "Speech recognition & synthesis" },
    { value: "elevenlabs", label: "ElevenLabs", description: "Ultra-realistic voices" },
    { value: "seamless-m4t", label: "Meta SeamlessM4T", description: "Multilingual translation & speech" },
    { value: "indic-tts", label: "AI4Bharat Indic TTS/STT", description: "Indian language support" },
    { value: "coqui-tts", label: "Coqui TTS", description: "Open-source TTS" },
  ],
};

// Validation rules for required fields
export const REQUIRED_FIELDS = {
  text: {
    common: ["goal", "subject"],
    models: {
      "gpt-4": [],
      "llama-3": [],
      "mistral": [],
      "gemini": [],
      "claude": [],
    },
  },
  image: {
    common: ["subject", "style"],
    models: {
      "dalle": [],
      "stable-diffusion": [],
      "midjourney": [],
      "imagen": [],
      "firefly": [],
    },
  },
  video: {
    common: ["scene", "action", "duration_seconds"],
    models: {
      "sora": [],
      "runway": ["camera_motion"],
      "pika": [],
      "veo": [],
      "stable-video-diffusion": [],
    },
  },
  audio: {
    common: ["subject", "accent", "emotion", "pace"],
    models: {
      "openai-audio": [],
      "elevenlabs": [],
      "seamless-m4t": [],
      "indic-tts": [],
      "coqui-tts": [],
    },
  },
};

// Field definitions for dynamic form generation
export const FIELD_DEFINITIONS = {
  text: [
    { name: "goal", label: "Goal", placeholder: "e.g., Write a blog post, Generate code, Analyze data", required: true, type: "text" },
    { name: "subject", label: "Subject", placeholder: "e.g., AI in healthcare, Python web scraper", required: true, type: "textarea" },
    { name: "task_type", label: "Task Type", placeholder: "e.g., creative writing, code generation, analysis", type: "text" },
    { name: "tone", label: "Tone", placeholder: "e.g., formal, casual, technical, friendly", type: "text" },
    { name: "format", label: "Output Format", placeholder: "e.g., markdown, json, plain text, code", type: "text" },
    { name: "length", label: "Length", placeholder: "short, medium, long", type: "select", options: ["short", "medium", "long"] },
    { name: "context", label: "Additional Context", placeholder: "Any background information or constraints", type: "textarea" },
    { name: "style", label: "Writing Style", placeholder: "e.g., concise, detailed, conversational", type: "text" },
  ],
  image: [
    { name: "subject", label: "Subject", placeholder: "e.g., a cat sitting on a windowsill", required: true, type: "text" },
    { name: "style", label: "Style", placeholder: "e.g., photorealistic, oil painting, anime", required: true, type: "text" },
    { name: "environment", label: "Environment", placeholder: "e.g., modern apartment, forest clearing", type: "text" },
    { name: "lighting", label: "Lighting", placeholder: "e.g., golden hour, dramatic shadows", type: "text" },
    { name: "camera", label: "Camera", placeholder: "e.g., 50mm close-up, wide angle", type: "text" },
    { name: "mood", label: "Mood", placeholder: "e.g., peaceful, energetic, mysterious", type: "text" },
    { name: "aspect_ratio", label: "Aspect Ratio", placeholder: "e.g., 16:9, 1:1, 9:16", type: "text" },
  ],
  video: [
    { name: "scene", label: "Scene", placeholder: "Describe the scene", required: true, type: "text" },
    { name: "action", label: "Action", placeholder: "What's happening?", required: true, type: "text" },
    { name: "duration_seconds", label: "Duration (seconds)", placeholder: "5", required: true, type: "number", min: 1, max: 60 },
    { name: "camera_motion", label: "Camera Motion", placeholder: "e.g., slow pan, tracking shot", type: "text" },
    { name: "lighting", label: "Lighting", placeholder: "e.g., natural daylight, neon", type: "text" },
    { name: "style", label: "Style", placeholder: "e.g., cinematic, documentary", type: "text" },
  ],
  audio: [
    { name: "subject", label: "Text/Script", placeholder: "What should be spoken?", required: true, type: "textarea" },
    { name: "accent", label: "Accent/Language", placeholder: "e.g., American, British, Hindi, Tamil", required: true, type: "text" },
    { name: "emotion", label: "Emotion", placeholder: "e.g., calm, excited, serious", required: true, type: "text" },
    { name: "pace", label: "Pace", placeholder: "slow, medium, fast", required: true, type: "select", options: ["slow", "medium", "fast"] },
    { name: "voice_gender", label: "Voice Gender", placeholder: "male, female, neutral", type: "select", options: ["male", "female", "neutral"] },
    { name: "age_range", label: "Age Range", placeholder: "e.g., young adult, middle-aged, elderly", type: "text" },
    { name: "use_case", label: "Use Case", placeholder: "e.g., podcast, audiobook, announcement", type: "text" },
  ],
};

// Prompt templates
export const TEMPLATES = {
  text: {
    blog: {
      name: "Blog Post",
      values: {
        goal: "Write a blog post",
        subject: "The impact of AI on modern healthcare",
        task_type: "creative writing",
        tone: "professional",
        format: "markdown",
        length: "medium",
      },
    },
    code: {
      name: "Code Generation",
      values: {
        goal: "Generate a function",
        subject: "Sort an array of objects by date in Python",
        task_type: "code generation",
        tone: "technical",
        format: "python",
        length: "short",
      },
    },
    analysis: {
      name: "Data Analysis",
      values: {
        goal: "Analyze and summarize",
        subject: "Market trends in renewable energy sector",
        task_type: "analysis",
        tone: "formal",
        format: "markdown",
        length: "long",
      },
    },
  },
  image: {
    portrait: {
      name: "Portrait Photography",
      values: {
        subject: "a person",
        style: "professional portrait photography",
        lighting: "soft natural light",
        camera: "85mm f/1.8",
        mood: "confident and approachable",
      },
    },
    landscape: {
      name: "Landscape",
      values: {
        subject: "a mountain landscape",
        style: "landscape photography",
        environment: "alpine setting at sunrise",
        lighting: "golden hour",
        camera: "wide angle 24mm",
      },
    },
    fantasy: {
      name: "Fantasy Art",
      values: {
        subject: "a magical creature",
        style: "fantasy digital art",
        environment: "enchanted forest",
        lighting: "mystical glowing lights",
        mood: "ethereal and mysterious",
      },
    },
  },
  video: {
    cinematic: {
      name: "Cinematic Scene",
      values: {
        scene: "a dramatic urban environment",
        action: "person walking in slow motion",
        duration_seconds: 10,
        camera_motion: "slow dolly forward",
        lighting: "moody with strong shadows",
        style: "cinematic film look",
      },
    },
    nature: {
      name: "Nature Documentary",
      values: {
        scene: "wildlife in natural habitat",
        action: "animal interacting with environment",
        duration_seconds: 15,
        camera_motion: "smooth tracking shot",
        lighting: "natural daylight",
        style: "documentary realism",
      },
    },
  },
  audio: {
    podcast: {
      name: "Podcast Host",
      values: {
        subject: "Welcome to today's episode",
        accent: "American",
        emotion: "friendly and conversational",
        pace: "medium",
        voice_gender: "neutral",
        use_case: "podcast",
      },
    },
    audiobook: {
      name: "Audiobook Narrator",
      values: {
        subject: "Chapter one begins",
        accent: "British",
        emotion: "calm and engaging",
        pace: "slow",
        voice_gender: "male",
        use_case: "audiobook",
      },
    },
    multilingual: {
      name: "Multilingual Speech",
      values: {
        subject: "नमस्ते, आज हम बात करेंगे",
        accent: "Hindi",
        emotion: "friendly",
        pace: "medium",
        voice_gender: "female",
        use_case: "announcement",
      },
    },
  },
};
