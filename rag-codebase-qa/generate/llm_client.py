import os
from groq import Groq

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