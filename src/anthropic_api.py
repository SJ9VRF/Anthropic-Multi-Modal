This module will handle interactions with the Anthropic API.
# src/anthropic_api.py
import os
from llama_index.multi_modal_llms.anthropic import AnthropicMultiModal

class AnthropicAPI:
    def __init__(self, api_key, max_tokens=300):
        os.environ['ANTHROPIC_API_KEY'] = api_key
        self.client = AnthropicMultiModal(max_tokens=max_tokens)

    def complete(self, prompt, image_documents):
        return self.client.complete(prompt=prompt, image_documents=image_documents)
