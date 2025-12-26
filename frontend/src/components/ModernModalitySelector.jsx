import "../styles/ModernModalitySelector.css";

const modalities = [
  {
    id: "text",
    name: "Text",
    subtitle: "LLM",
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
        <polyline points="14 2 14 8 20 8" />
        <line x1="16" y1="13" x2="8" y2="13" />
        <line x1="16" y1="17" x2="8" y2="17" />
        <polyline points="10 9 9 9 8 9" />
      </svg>
    ),
    gradient: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    bgColor: "rgba(102, 126, 234, 0.1)",
    emoji: "📝",
  },
  {
    id: "image",
    name: "Image",
    subtitle: "Generation",
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
        <circle cx="8.5" cy="8.5" r="1.5" />
        <polyline points="21 15 16 10 5 21" />
      </svg>
    ),
    gradient: "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
    bgColor: "rgba(250, 112, 154, 0.1)",
    emoji: "🎨",
  },
  {
    id: "video",
    name: "Video",
    subtitle: "Creation",
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <polygon points="23 7 16 12 23 17 23 7" />
        <rect x="1" y="5" width="15" height="14" rx="2" ry="2" />
      </svg>
    ),
    gradient: "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
    bgColor: "rgba(240, 147, 251, 0.1)",
    emoji: "🎬",
  },
  {
    id: "audio",
    name: "Audio",
    subtitle: "Synthesis",
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
        <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
        <line x1="12" y1="19" x2="12" y2="23" />
        <line x1="8" y1="23" x2="16" y2="23" />
      </svg>
    ),
    gradient: "linear-gradient(135deg, #4ade80 0%, #22c55e 100%)",
    bgColor: "rgba(74, 222, 128, 0.1)",
    emoji: "🎙️",
  },
];

/**
 * Ultra-Modern Modality Selector - Single Line with Beautiful Cards
 */
function ModernModalitySelector({ modality, onModalityChange }) {
  return (
    <div className="modality-selector-v2">
      {/* Floating Particles Background */}
      <div className="particles-bg">
        {[...Array(5)].map((_, i) => (
          <div key={i} className={`particle particle-${i + 1}`}></div>
        ))}
      </div>

      {/* Header Section */}
      <div className="selector-header-v2">
        <div className="header-badge">
          <span className="pulse-dot"></span>
          <span>Choose Your AI</span>
        </div>
        <h2 className="selector-title-v2">
          <span className="title-line">Select Your</span>
          <span className="title-highlight gradient-text">Creative Medium</span>
        </h2>
        <p className="selector-subtitle-v2">
          Transform your ideas into reality with AI-powered generation
        </p>
      </div>

      {/* Modality Cards - Single Line */}
      <div className="modality-cards-v2">
        {modalities.map((mod, index) => (
          <button
            key={mod.id}
            className={`modality-card-v2 ${
              modality === mod.id ? "active" : ""
            }`}
            onClick={() => onModalityChange(mod.id)}
            style={{
              animationDelay: `${index * 0.1}s`,
            }}
            aria-pressed={modality === mod.id}
            aria-label={`Select ${mod.name} modality`}
          >
            {/* Card Background with Gradient */}
            <div
              className="card-bg-gradient"
              style={{ background: mod.gradient }}
            ></div>

            {/* Emoji Badge */}
            <div className="card-emoji">{mod.emoji}</div>

            {/* Icon Container */}
            <div className="card-icon-container">
              <div className="card-icon-v2">{mod.icon}</div>
            </div>

            {/* Card Text */}
            <div className="card-text">
              <h3 className="card-title-v2">{mod.name}</h3>
              <p className="card-subtitle-v2">{mod.subtitle}</p>
            </div>

            {/* Active Indicator Checkmark */}
            {modality === mod.id && (
              <div className="active-check">
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="3"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <polyline points="20 6 9 17 4 12" />
                </svg>
              </div>
            )}

            {/* Shimmer Effect */}
            <div className="card-shimmer"></div>

            {/* Glow on Hover */}
            <div
              className="card-glow-v2"
              style={{ background: mod.gradient }}
            ></div>
          </button>
        ))}
      </div>

      {/* Bottom Decorative Line */}
      <div className="selector-divider">
        <div className="divider-glow"></div>
      </div>
    </div>
  );
}

export default ModernModalitySelector;
