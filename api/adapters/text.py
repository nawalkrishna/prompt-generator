"""Text generation adapters for different LLM models."""

from schema import TextPrompt


class GPT4Adapter:
    """OpenAI GPT-4 / GPT-4.1 / GPT-4o adapter."""

    model_name = "gpt-4"

    def compile(self, p: TextPrompt) -> str:
        prompt = f"{p.goal}: {p.subject}"

        details = []
        if p.task_type:
            details.append(f"Type: {p.task_type}")
        if p.context:
            details.append(f"Context: {p.context}")
        if p.style:
            details.append(f"Style: {p.style}")
        if p.tone:
            details.append(f"Tone: {p.tone}")
        if p.format:
            details.append(f"Format: {p.format}")
        if p.length:
            details.append(f"Length: {p.length}")
        if p.constraints:
            details.append(f"Must include: {', '.join(p.constraints)}")

        if details:
            prompt += "\n\n" + "\n".join(details)

        if p.negative_constraints:
            prompt += f"\n\nDo not: {', '.join(p.negative_constraints)}"

        return prompt


class LlamaAdapter:
    """Meta LLaMA 3 adapter."""

    model_name = "llama-3"

    def compile(self, p: TextPrompt) -> str:
        # Llama works best with clear instruction format
        instruction = f"[INST] {p.goal}\n\n"
        instruction += f"Topic: {p.subject}\n"

        if p.task_type:
            instruction += f"Task: {p.task_type}\n"
        if p.context:
            instruction += f"Background: {p.context}\n"

        instruction += "\n"

        if p.style or p.tone or p.format:
            instruction += "Guidelines:\n"
            if p.style:
                instruction += f"- Use {p.style} style\n"
            if p.tone:
                instruction += f"- Maintain {p.tone} tone\n"
            if p.format:
                instruction += f"- Output in {p.format} format\n"
            if p.length:
                instruction += f"- Keep it {p.length}\n"

        if p.constraints:
            instruction += f"\nMust include: {', '.join(p.constraints)}\n"

        if p.negative_constraints:
            instruction += f"Avoid: {', '.join(p.negative_constraints)}\n"

        instruction += " [/INST]"

        return instruction


class MistralAdapter:
    """Mistral AI Mistral / Mixtral adapter."""

    model_name = "mistral"

    def compile(self, p: TextPrompt) -> str:
        # Mistral prefers concise, direct prompts
        prompt_parts = []

        # Core task
        if p.task_type:
            prompt_parts.append(f"{p.task_type.title()}: {p.goal}")
        else:
            prompt_parts.append(p.goal)

        prompt_parts.append(f"\nTopic: {p.subject}")

        if p.context:
            prompt_parts.append(f"\n{p.context}")

        # Specifications in compact format
        specs = []
        if p.style:
            specs.append(f"style={p.style}")
        if p.tone:
            specs.append(f"tone={p.tone}")
        if p.format:
            specs.append(f"format={p.format}")
        if p.length:
            specs.append(f"length={p.length}")

        if specs:
            prompt_parts.append(f"\n[{', '.join(specs)}]")

        if p.constraints:
            prompt_parts.append(f"\nInclude: {'; '.join(p.constraints)}")

        if p.negative_constraints:
            prompt_parts.append(f"\nExclude: {'; '.join(p.negative_constraints)}")

        return "".join(prompt_parts)


class GeminiAdapter:
    """Google Gemini adapter."""

    model_name = "gemini"

    def compile(self, p: TextPrompt) -> str:
        parts = [f"## {p.goal}"]
        parts.append(f"**Subject:** {p.subject}")

        if p.task_type:
            parts.append(f"**Task Type:** {p.task_type}")

        if p.context:
            parts.append(f"**Context:**\n{p.context}")

        specifications = []
        if p.style:
            specifications.append(f"- Style: {p.style}")
        if p.tone:
            specifications.append(f"- Tone: {p.tone}")
        if p.format:
            specifications.append(f"- Format: {p.format}")
        if p.length:
            specifications.append(f"- Length: {p.length}")
        if p.quality_level:
            specifications.append(f"- Quality: {p.quality_level}")

        if specifications:
            parts.append("**Specifications:**")
            parts.extend(specifications)

        if p.constraints:
            parts.append(f"**Requirements:** {', '.join(p.constraints)}")

        if p.negative_constraints:
            parts.append(f"**Exclude:** {', '.join(p.negative_constraints)}")

        return "\n".join(parts)


class ClaudeAdapter:
    """Anthropic Claude adapter."""

    model_name = "claude"

    def compile(self, p: TextPrompt) -> str:
        parts = []

        # Start with clear task description
        if p.task_type:
            parts.append(f"Task: {p.task_type}")

        parts.append(f"Goal: {p.goal}")
        parts.append(f"Subject: {p.subject}")

        # Add context if provided
        if p.context:
            parts.append(f"Context: {p.context}")

        # Add style and tone
        if p.style:
            parts.append(f"Style: {p.style}")
        if p.tone:
            parts.append(f"Tone: {p.tone}")

        # Add constraints
        if p.constraints:
            parts.append(f"Requirements: {', '.join(p.constraints)}")

        # Add format and length
        if p.format:
            parts.append(f"Output format: {p.format}")
        if p.length:
            parts.append(f"Length: {p.length}")

        # Add quality level
        if p.quality_level:
            parts.append(f"Quality: {p.quality_level}")

        # Add negative constraints
        if p.negative_constraints:
            parts.append(f"Avoid: {', '.join(p.negative_constraints)}")

        return "\n".join(parts)
