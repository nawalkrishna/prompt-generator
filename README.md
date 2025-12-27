# AI Prompt Generator

A powerful, full-stack application for generating optimized prompts for various AI models across image, video, and voice modalities.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![React](https://img.shields.io/badge/react-19.x-blue.svg)

Website link: https://prompt-generator-1234.vercel.app/


## Features

### Core Functionality
- **Multi-Modal Support**: Generate prompts for Image, Video, and Voice AI models
- **10 AI Models**: Support for DALL-E 3, Midjourney v6, SDXL, Imagen, Firefly, Runway Gen-3, Pika, Sora, OpenAI Voice, and ElevenLabs
- **Model-Specific Formatting**: Each adapter optimizes prompts for specific model requirements
- **Real-Time Validation**: Input validation with helpful error messages
- **Template System**: Quick-start templates for common use cases

### User Experience
- **Toast Notifications**: Non-intrusive feedback for user actions
- **Prompt History**: Save and manage generated prompts with favorites
- **Export Functionality**: Download prompts as TXT or JSON files
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Accessibility**: ARIA labels, keyboard navigation, and screen reader support
- **Dark Theme**: Modern, eye-friendly interface

### Developer Features
- **Type Safety**: JSDoc type definitions throughout
- **Centralized Configuration**: Single source of truth for models and validation
- **Comprehensive Logging**: Backend logging for debugging and monitoring
- **API Error Handling**: Structured error responses with proper HTTP status codes
- **Environment Configuration**: Easy deployment configuration

## Architecture

### Backend (Python/Flask)
```
backend/
├── adapters/          # Model-specific prompt formatters
│   ├── image.py      # 5 image model adapters
│   ├── video.py      # 3 video model adapters
│   └── voice.py      # 2 voice model adapters
├── app.py            # Flask API with validation
├── compiler.py       # Prompt compilation orchestrator
├── schema.py         # Dataclass models
├── registry.py       # Adapter registry
└── .env.example      # Environment configuration template
```

### Frontend (React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── ImprovedPromptForm.jsx    # Dynamic form with templates
│   │   ├── ImprovedResultBox.jsx     # Result display with export
│   │   ├── History.jsx               # History management
│   │   ├── Toast.jsx                 # Toast notifications
│   │   └── ModalitySelector.jsx      # Modality switcher
│   ├── hooks/
│   │   ├── useToast.js               # Toast management hook
│   │   └── useLocalStorage.js        # LocalStorage sync hook
│   ├── styles/                       # Component-specific CSS
│   ├── config.js                     # Central configuration
│   ├── validation.js                 # Validation utilities
│   ├── api.js                        # API client
│   └── types.js                      # JSDoc type definitions
└── .env.example                      # Environment template
```

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create environment file:
```bash
cp .env.example .env
```

6. Start the server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Start the development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## Usage

### Basic Workflow

1. **Select Modality**: Choose between Image, Video, or Voice
2. **Choose Template** (Optional): Start with a pre-configured template
3. **Fill Form**: Enter required fields for your prompt
4. **Select Model**: Choose the AI model you're targeting
5. **Generate**: Click "Generate Prompt" to create optimized prompt
6. **Export or Save**: Copy, export, or save to history

### API Endpoints

#### Generate Prompt
```http
POST /generate
Content-Type: application/json

{
  "modality": "image",
  "model": "dalle-3",
  "payload": {
    "subject": "a cat",
    "style": "photorealistic",
    "lighting": "golden hour"
  }
}
```

#### Get Available Models
```http
GET /models
```

#### Health Check
```http
GET /health
```

### Examples

#### Image Generation (Midjourney)
```javascript
{
  "modality": "image",
  "model": "midjourney-v6",
  "payload": {
    "subject": "a futuristic cityscape",
    "style": "cyberpunk",
    "lighting": "neon lights",
    "mood": "mysterious",
    "aspect_ratio": "16:9"
  }
}
```

Output:
```
a futuristic cityscape, cyberpunk, neon lights, mysterious --ar 16:9 --v 6 --q 2
```

#### Video Generation (Sora)
```javascript
{
  "modality": "video",
  "model": "sora",
  "payload": {
    "scene": "a busy city street at night",
    "action": "people walking with umbrellas in the rain",
    "camera_motion": "slowly pans across the scene",
    "duration_seconds": 10
  }
}
```

#### Voice Synthesis (ElevenLabs)
```javascript
{
  "modality": "voice",
  "model": "elevenlabs",
  "payload": {
    "subject": "Welcome to our podcast",
    "accent": "American",
    "emotion": "friendly",
    "pace": "medium",
    "voice_gender": "female"
  }
}
```

## Configuration

### Backend Environment Variables

```env
# Flask Configuration
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
FLASK_DEBUG=False

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000

# Rate Limiting
RATE_LIMIT=60
```

### Frontend Environment Variables

```env
# API Configuration
REACT_APP_API_URL=http://localhost:5000

# Feature Flags
REACT_APP_ENABLE_HISTORY=true
REACT_APP_ENABLE_TEMPLATES=true
```

## Supported Models

### Image Models
| Model | ID | Best For |
|-------|-----|----------|
| DALL-E 3 | `dalle-3` | Natural language descriptions |
| Midjourney v6 | `midjourney-v6` | Artistic, high-quality images |
| Stable Diffusion XL | `sdxl` | Customizable, open-source |
| Google Imagen | `imagen` | Photorealistic images |
| Adobe Firefly | `firefly` | Commercial-safe content |

### Video Models
| Model | ID | Best For |
|-------|-----|----------|
| Runway Gen-3 | `runway-gen3` | Cinematic videos |
| Pika | `pika` | Quick video creation |
| OpenAI Sora | `sora` | Coherent, long-form videos |

### Voice Models
| Model | ID | Best For |
|-------|-----|----------|
| OpenAI Voice | `openai-voice` | Natural text-to-speech |
| ElevenLabs | `elevenlabs` | Ultra-realistic voices |

## Development

### Adding a New Model

1. **Create Adapter** (`backend/adapters/{modality}.py`):
```python
class NewModelAdapter:
    model_name = "new-model"

    def compile(self, p: PromptType) -> str:
        # Format prompt for this model
        return formatted_prompt
```

2. **Register Adapter** (`backend/registry.py`):
```python
ADAPTER_REGISTRY["new-model"] = NewModelAdapter()
```

3. **Update Config** (`frontend/src/config.js`):
```javascript
export const MODELS = {
  modality: [
    // ... existing models
    {
      value: "new-model",
      label: "New Model",
      description: "Description"
    },
  ],
};
```

4. **Add Validation Rules** (if needed in `config.js`):
```javascript
export const REQUIRED_FIELDS = {
  modality: {
    common: ["field1", "field2"],
    models: {
      "new-model": ["special-field"],
    },
  },
};
```

### Running Tests

Backend tests:
```bash
cd backend
pytest
```

Frontend tests:
```bash
cd frontend
npm test
```

## Deployment

### Production Backend

1. Set production environment variables
2. Use a production WSGI server (gunicorn):
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. Configure reverse proxy (nginx/Apache)
4. Enable HTTPS
5. Set up rate limiting

### Production Frontend

1. Build the production bundle:
```bash
npm run build
```

2. Serve static files with nginx/Apache
3. Configure environment variables
4. Enable gzip compression
5. Set up CDN (optional)

## Troubleshooting

### Common Issues

**Backend won't start**
- Check Python version (3.8+)
- Verify all dependencies installed
- Check if port 5000 is available

**Frontend can't connect to backend**
- Verify backend is running
- Check CORS configuration
- Verify API_BASE_URL in frontend .env

**Validation errors**
- Check required fields for selected model
- Verify field names match schema
- Check browser console for details

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- Built with Flask and React
- Inspired by the prompt engineering community
- Icons from Heroicons

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review closed issues

---

**Made with ❤️ for the AI community**
