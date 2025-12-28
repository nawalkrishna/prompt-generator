"""Audio generation adapters for different AI models."""

from schema import VoicePrompt


class OpenAIAudioAdapter:
    """OpenAI Whisper + TTS adapter."""

    model_name = "openai-audio"

    def compile(self, p: VoicePrompt) -> str:
        parts = []

        if p.emotion:
            if p.voice_gender:
                parts.append(f"Use a {p.emotion} {p.voice_gender} voice")
            else:
                parts.append(f"Use a {p.emotion} voice")
        elif p.voice_gender:
            parts.append(f"Use a {p.voice_gender} voice")

        if p.accent:
            parts.append(f"with a {p.accent} accent")

        if p.pace:
            parts.append(f"Pace: {p.pace}")

        if p.use_case:
            parts.append(f"Purpose: {p.use_case}")

        if p.age_range:
            parts.append(f"Age range: {p.age_range}")

        return ". ".join(parts) + "." if parts else "Generate natural voice."


class ElevenLabsAdapter:
    """ElevenLabs adapter."""

    model_name = "elevenlabs"

    def compile(self, p: VoicePrompt) -> str:
        lines = []

        if p.voice_gender:
            lines.append(f"Voice: {p.voice_gender}")

        if p.accent:
            lines.append(f"Accent: {p.accent}")

        if p.emotion:
            lines.append(f"Emotion: {p.emotion}")

        if p.pace:
            lines.append(f"Pace: {p.pace}")

        if p.age_range:
            lines.append(f"Age: {p.age_range}")

        # ElevenLabs-specific parameters
        lines.append("Stability: 70%")
        lines.append("Clarity: High")

        return "\n".join(lines)


class SeamlessM4TAdapter:
    """Meta SeamlessM4T adapter - multilingual speech and translation."""

    model_name = "seamless-m4t"

    def compile(self, p: VoicePrompt) -> str:
        parts = []

        # SeamlessM4T focuses on multilingual capabilities
        if p.accent:
            parts.append(f"Language/Accent: {p.accent}")

        if p.voice_gender:
            parts.append(f"Voice type: {p.voice_gender}")

        if p.emotion:
            parts.append(f"Emotional expression: {p.emotion}")

        if p.pace:
            parts.append(f"Speech rate: {p.pace}")

        if p.use_case:
            parts.append(f"Application: {p.use_case}")

        if p.style:
            parts.append(f"Speaking style: {p.style}")

        return " | ".join(parts) if parts else "Generate multilingual speech"


class IndicTTSAdapter:
    """AI4Bharat Indic TTS / STT adapter - Indian language support."""

    model_name = "indic-tts"

    def compile(self, p: VoicePrompt) -> str:
        lines = []

        # Indic TTS specializes in Indian languages
        if p.accent:
            lines.append(f"Language: {p.accent}")

        if p.voice_gender:
            lines.append(f"Voice: {p.voice_gender}")

        if p.age_range:
            lines.append(f"Age group: {p.age_range}")

        if p.emotion:
            lines.append(f"Emotion: {p.emotion}")

        if p.pace:
            lines.append(f"Speaking pace: {p.pace}")

        if p.use_case:
            lines.append(f"Use case: {p.use_case}")

        if p.style:
            lines.append(f"Style: {p.style}")

        return "\n".join(lines) if lines else "Generate Indic language speech"


class CoquiTTSAdapter:
    """Coqui TTS adapter - open-source text-to-speech."""

    model_name = "coqui-tts"

    def compile(self, p: VoicePrompt) -> str:
        parts = ["Coqui TTS Configuration"]

        voice_desc = []
        if p.voice_gender:
            voice_desc.append(p.voice_gender)
        if p.age_range:
            voice_desc.append(f"age {p.age_range}")
        if p.accent:
            voice_desc.append(f"{p.accent} accent")

        if voice_desc:
            parts.append(f"Voice: {', '.join(voice_desc)}")

        if p.emotion:
            parts.append(f"Emotion: {p.emotion}")

        if p.pace:
            parts.append(f"Speed: {p.pace}")

        if p.style:
            parts.append(f"Style: {p.style}")

        if p.use_case:
            parts.append(f"Target use: {p.use_case}")

        return " | ".join(parts)
