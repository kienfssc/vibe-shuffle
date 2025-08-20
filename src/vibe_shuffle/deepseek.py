import os
from typing_extensions import Literal
import openai
from typing import TypeVar
import json
from dataclasses import dataclass

@dataclass
class DeepseekVibeShuffleResponse:
    shuffled_array: list[int]

@dataclass
class DeepseekVibeShuffleRequest:
    array: list[int]
    instruction: Literal["shuffle the array and then return json format without any additional information"] = "shuffle the array and then return json format without any additional information"
    
    def model_dump_json(self) -> str:
        """Convert to JSON string for compatibility"""
        return json.dumps({
            "array": self.array,
            "instruction": self.instruction
        })
    
def structured_output_deepseek(
    content: str,
    model: str = "deepseek-chat",
):
    api_key = os.environ["DEEPSEEK_API_KEY"]
    base_url = os.environ.get("DEEPSEEK_API_BASE_URL", "https://api.deepseek.com/v1")
    client = openai.OpenAI(api_key=api_key, base_url=base_url)
    
    # Remove response_format parameter completely - DeepSeek doesn't support it
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"{content}\n\nReturn only valid JSON with 'shuffled_array' field containing the shuffled array."
            }
        ],
        temperature=0.1
    )
    
    # Parse the response manually
    response_text = response.choices[0].message.content
    
    try:
        # Clean the response (remove markdown if present)
        cleaned_text = response_text.strip()
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[7:]
        if cleaned_text.endswith("```"):
            cleaned_text = cleaned_text[:-3]
        cleaned_text = cleaned_text.strip()
        
        # Parse JSON and create dataclass instance
        json_data = json.loads(cleaned_text)
        return DeepseekVibeShuffleResponse(**json_data) 
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse JSON from response: {response_text}\nError: {e}")

def deepseek_vibe_shuffle(array: list[int]) -> list[int]:
    response = structured_output_deepseek(
        content=DeepseekVibeShuffleRequest(array=array).model_dump_json(),
    )
    return response.shuffled_array