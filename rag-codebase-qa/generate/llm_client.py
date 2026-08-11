import os
from groq import Groq

# Load .env file if GROQ_API_KEY is not in the environment
if not os.getenv("GROQ_API_KEY"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while current_dir:
        env_path = os.path.join(current_dir, ".env")
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ[k.strip()] = v.strip()
            break
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            break
        current_dir = parent_dir

api_key = os.getenv("GROQ_API_KEY")
_client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"  # free tier, good quality for this task

def call_llm(system_prompt, user_prompt, temperature=0.1):
    response = _client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,  # low temp — this is a factual task, not creative
    )
    return response.choices[0].message.content