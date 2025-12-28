from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CanonicalPrompt:
    modality: str
    goal: str
    subject: str
    style: Optional[str] = None
    constraints: Optional[List[str]] = None
    negative_constraints: Optional[List[str]] = None
    quality_level: Optional[str] = None


@dataclass
class ImagePrompt(CanonicalPrompt):
    environment: Optional[str] = None
    lighting: Optional[str] = None
    camera: Optional[str] = None
    mood: Optional[str] = None
    aspect_ratio: Optional[str] = None


@dataclass
class VideoPrompt(CanonicalPrompt):
    scene: str = ""
    action: str = ""
    camera_motion: Optional[str] = None
    lighting: Optional[str] = None
    duration_seconds: int = 5
    realism_level: Optional[str] = None


@dataclass
class VoicePrompt(CanonicalPrompt):
    voice_gender: Optional[str] = None
    age_range: Optional[str] = None
    accent: Optional[str] = None
    emotion: Optional[str] = None
    pace: Optional[str] = None
    use_case: Optional[str] = None


@dataclass
class TextPrompt(CanonicalPrompt):
    task_type: Optional[str] = None  # e.g., "creative writing", "code generation", "analysis"
    tone: Optional[str] = None  # e.g., "formal", "casual", "technical"
    format: Optional[str] = None  # e.g., "markdown", "json", "plain text"
    length: Optional[str] = None  # e.g., "short", "medium", "long"
    context: Optional[str] = None  # additional context for the task
