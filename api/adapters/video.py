"""Video generation adapters for different AI models."""

from schema import VideoPrompt


class SoraAdapter:
    """OpenAI Sora adapter."""

    model_name = "sora"

    def compile(self, p: VideoPrompt) -> str:
        parts = [f"A coherent {p.duration_seconds}-second cinematic video of {p.scene}"]

        if p.action:
            parts.append(f"The subject is {p.action}")

        if p.camera_motion:
            parts.append(f"The camera {p.camera_motion}")

        if p.lighting:
            parts.append(f"Lighting is {p.lighting}")

        if p.style:
            parts.append(f"Style: {p.style}")

        return ". ".join(parts) + "."


class RunwayAdapter:
    """Runway Gen-2 / Gen-3 adapter."""

    model_name = "runway"

    def compile(self, p: VideoPrompt) -> str:
        parts = [f"A {p.duration_seconds}-second cinematic scene of {p.scene}"]

        if p.action:
            parts.append(f"Action: {p.action}")

        if p.camera_motion:
            parts.append(f"Camera: {p.camera_motion}")

        if p.lighting:
            parts.append(f"Lighting: {p.lighting}")

        parts.append("Realistic motion")

        return ". ".join(parts) + "."


class PikaAdapter:
    """Pika Labs Pika adapter."""

    model_name = "pika"

    def compile(self, p: VideoPrompt) -> str:
        lines = [f"Scene: {p.scene}"]

        if p.action:
            lines.append(f"Action: {p.action}")

        if p.camera_motion:
            lines.append(f"Camera movement: {p.camera_motion}")

        if p.style:
            lines.append(f"Style: {p.style}")

        lines.append(f"Duration: {p.duration_seconds}s")

        return "\n".join(lines)


class VeoAdapter:
    """Google Veo adapter."""

    model_name = "veo"

    def compile(self, p: VideoPrompt) -> str:
        parts = [f"Generate {p.duration_seconds}s video"]
        parts.append(f"Scene: {p.scene}")

        if p.action:
            parts.append(f"Action: {p.action}")

        if p.camera_motion:
            parts.append(f"Camera: {p.camera_motion}")

        if p.lighting:
            parts.append(f"Lighting: {p.lighting}")

        if p.style:
            parts.append(f"Visual style: {p.style}")

        if p.realism_level:
            parts.append(f"Realism: {p.realism_level}")

        return " | ".join(parts)


class StableVideoDiffusionAdapter:
    """Stable Video Diffusion adapter."""

    model_name = "stable-video-diffusion"

    def compile(self, p: VideoPrompt) -> str:
        positive_parts = [p.scene]

        if p.action:
            positive_parts.append(p.action)
        if p.style:
            positive_parts.append(p.style)
        if p.lighting:
            positive_parts.append(p.lighting)
        if p.camera_motion:
            positive_parts.append(f"camera {p.camera_motion}")

        positive = ", ".join(positive_parts)
        negative = ", ".join(p.negative_constraints or ["low quality", "blurry", "artifacts"])

        return f"Positive: {positive}\nNegative: {negative}\nFrames: {p.duration_seconds * 24}"
