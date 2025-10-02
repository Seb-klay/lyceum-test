import requests
import os

# since passing env variables is yet not available, you just send it raw AS A TEST
BEARER_TOKEN="YOUR_API_KEY"

response = requests.post(
    "https://api.lyceum.technology/api/v2/external/execution/image/start",
    headers={"Authorization": f"Bearer {BEARER_TOKEN}"},
    json={
        "docker_image_ref": "ollama/ollama",
        "docker_run_cmd": ["ollama", "serve", "tinyllama", "--prompt", "Hello from Ollama!"],
        "execution_type": "cpu"
    }
)


res = response.json()
print(f"Started execution: {res}")

with requests.get(res.streaming_url, stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode("utf-8"))