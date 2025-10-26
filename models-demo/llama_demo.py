import os
from llama_api_client import LlamaAPIClient


client = LlamaAPIClient(
    api_key=os.environ.get("LLAMA_API_KEY"),
    base_url="https://api.llama.com/v1/",
)

messages = [
    {"role": "user", "content": "Hello! Can you help me with Python?"}
]

response = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=messages
)


print(response)

content = response.completion_message.content.text
print(content)