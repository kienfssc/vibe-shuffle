import os
from . import deepseek

def vibe_shuffle(array: list[int]):
    method = os.environ.get("DEFAULT_VIBE_SHUFFLE_METHOD", "deepseek")

    match method:
        case "deepseek":
            # Handle deepseek method
            return deepseek.deepseek_vibe_shuffle(array)
        case "openai":
            raise NotImplementedError("OpenAI method is not implemented yet.")
        case _:
            raise ValueError(f"Unsupported method: {method}")