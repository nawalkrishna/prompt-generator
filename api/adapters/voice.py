"""Voice synthesis adapters for different AI models."""

from schema import VoicePrompt


class OpenAIVoiceAdapter:
    """OpenAI Voice adapter - natural language descriptions."""

    model_name = "openai-voice"

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
    """ElevenLabs adapter - structured parameter format."""

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


class PlayHTAdapter:
    """Play.ht adapter - AI voice generation platform."""

    model_name = "playht"

    def compile(self, p: VoicePrompt) -> str:
        parts = []

        characteristics = []
        if p.voice_gender:
            characteristics.append(p.voice_gender)
        if p.age_range:
            characteristics.append(p.age_range)
        if p.accent:
            characteristics.append(f"{p.accent} accent")

        if characteristics:
            parts.append(f"Voice: {', '.join(characteristics)}")

        if p.emotion:
            parts.append(f"Emotional tone: {p.emotion}")

        if p.pace:
            parts.append(f"Speaking pace: {p.pace}")

        if p.use_case:
            parts.append(f"Use case: {p.use_case}")

        if p.style:
            parts.append(f"Style: {p.style}")

        return " | ".join(parts) if parts else "Generate natural voice"


class AzureVoiceAdapter:
    """Azure Speech Services adapter - Microsoft's TTS platform."""

    model_name = "azure-voice"

    def compile(self, p: VoicePrompt) -> str:
        prompt = "Voice characteristics: "

        specs = []
        if p.voice_gender:
            specs.append(f"gender={p.voice_gender}")
        if p.age_range:
            specs.append(f"age={p.age_range}")
        if p.accent:
            specs.append(f"locale={p.accent}")
        if p.emotion:
            specs.append(f"style={p.emotion}")
        if p.pace:
            specs.append(f"rate={p.pace}")

        prompt += ", ".join(specs) if specs else "natural"

        if p.use_case:
            prompt += f" | Purpose: {p.use_case}"

        return prompt


class MurfAIAdapter:
    """Murf.AI adapter - professional voiceover platform."""

    model_name = "murfai"

    def compile(self, p: VoicePrompt) -> str:
        parts = ["Professional voiceover"]

        if p.voice_gender:
            parts.append(f"{p.voice_gender} voice")

        if p.age_range:
            parts.append(f"age {p.age_range}")

        if p.accent:
            parts.append(f"with {p.accent} accent")

        if p.emotion:
            parts.append(f"expressing {p.emotion}")

        if p.pace:
            parts.append(f"at {p.pace} pace")

        if p.use_case:
            parts.append(f"for {p.use_case}")

        return ", ".join(parts) + "."


class WellSaidAdapter:
    """WellSaid Labs adapter - enterprise voice synthesis."""

    model_name = "wellsaid"

    def compile(self, p: VoicePrompt) -> str:
        lines = []

        # Create voice profile description
        profile = []
        if p.voice_gender:
            profile.append(p.voice_gender)
        if p.age_range:
            profile.append(f"aged {p.age_range}")

        if profile:
            lines.append(f"Voice Profile: {' '.join(profile)}")

        if p.accent:
            lines.append(f"Accent: {p.accent}")

        if p.emotion:
            lines.append(f"Emotional delivery: {p.emotion}")

        if p.pace:
            lines.append(f"Delivery pace: {p.pace}")

        if p.style:
            lines.append(f"Speaking style: {p.style}")

        if p.use_case:
            lines.append(f"Application: {p.use_case}")

        # WellSaid-specific quality settings
        lines.append("Audio quality: Studio")

        return "\n".join(lines)
