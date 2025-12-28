from registry import ADAPTER_REGISTRY


class PromptCompiler:
    def compile(self, prompt, model_name: str) -> str:
        adapter = ADAPTER_REGISTRY.get(model_name)
        if not adapter:
            raise ValueError(f"Unsupported model: {model_name}")
        return adapter.compile(prompt)
