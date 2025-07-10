import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

def generate_code(task, step_index=0):
    prompt = f"""
{task}

Scrivi ogni file nel formato:

--- percorso/nomefile.ext ---
<codice>

Non scrivere spiegazioni.
"""

    print("🚀 Invio richiesta al modello AI...")

    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    code = response.choices[0].message.content
    save_output(code, step_index)

def save_output(text, step_index=0):
    os.makedirs("generated_projects", exist_ok=True)
    filename = f"output_step_{step_index}.txt"
    path = os.path.join("generated_projects", filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
        print(f"✅ Output salvato in: {path}")
