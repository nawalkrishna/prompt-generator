"""Image generation adapters for different AI models."""

from schema import ImagePrompt


class DalleAdapter:
    """DALL-E 3 adapter - uses natural language with detailed descriptions."""

    model_name = "dalle-3"

    def compile(self, p: ImagePrompt) -> str:
        parts = [f"Create a {p.style or 'detailed'} image of {p.subject}"]

        if p.environment:
            parts.append(f"in {p.environment}")

        details = []
        if p.lighting:
            details.append(f"Lighting: {p.lighting}")
        if p.mood:
            details.append(f"Mood: {p.mood}")
        if p.camera:
            details.append(f"Camera: {p.camera}")
        if p.quality_level:
            details.append(f"Quality: {p.quality_level}")

        if details:
            parts.append(". ".join(details))

        if p.negative_constraints:
            parts.append(f"Avoid: {', '.join(p.negative_constraints)}")

        return ". ".join(parts) + "."


class MidjourneyAdapter:
    """Midjourney v6 adapter - uses comma-separated tags with parameters."""

    model_name = "midjourney-v6"

    def compile(self, p: ImagePrompt) -> str:
        parts = [p.subject]

        if p.environment:
            parts.append(p.environment)
        if p.style:
            parts.append(p.style)
        if p.lighting:
            parts.append(p.lighting)
        if p.camera:
            parts.append(p.camera)
        if p.mood:
            parts.append(p.mood)

        prompt = ", ".join(parts)

        # Add Midjourney-specific parameters
        params = []
        params.append(f"--ar {p.aspect_ratio or '16:9'}")
        params.append("--v 6")
        params.append("--q 2")

        return f"{prompt} {' '.join(params)}"


class StableDiffusionAdapter:
    """Stable Diffusion XL adapter - uses separate positive/negative prompts."""

    model_name = "sdxl"

    def compile(self, p: ImagePrompt) -> str:
        positive_parts = [p.subject]

        if p.environment:
            positive_parts.append(p.environment)
        if p.style:
            positive_parts.append(p.style)
        if p.lighting:
            positive_parts.append(p.lighting)
        if p.mood:
            positive_parts.append(p.mood)

        positive = ", ".join(positive_parts)
        negative = ", ".join(p.negative_constraints or ["low quality", "blurry"])

        return f"Positive: {positive}\nNegative: {negative}"


class ImagenAdapter:
    """Google Imagen adapter - focuses on realistic descriptions."""

    model_name = "imagen"

    def compile(self, p: ImagePrompt) -> str:
        parts = [f"A realistic image of {p.subject}"]

        if p.environment:
            parts.append(f"in {p.environment}")

        parts.append("natural lighting, realistic proportions")

        if p.style:
            parts.append(f"{p.style} style")

        return ", ".join(parts) + "."


class FireflyAdapter:
    """Adobe Firefly adapter - emphasizes commercial quality."""

    model_name = "firefly"

    def compile(self, p: ImagePrompt) -> str:
        parts = [f"High-quality commercial image of {p.subject}"]

        if p.environment:
            parts.append(f"in {p.environment}")

        parts.append("clean lighting, professional style")

        if p.style:
            parts.append(f"{p.style} aesthetic")

        return ", ".join(parts) + "."
