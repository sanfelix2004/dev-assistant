import os
import subprocess
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = "dev-assistant-project"
PROJECT_PATH = "generated_projects/project"

# Richiedi commit message all'AI
def generate_commit_message():
    client = OpenAI(
        api_key=os.getenv("TOGETHER_API_KEY"),
        base_url="https://api.together.xyz/v1"
    )

    prompt = "Genera un messaggio di commit significativo e conciso per un progetto Spring Boot con controller, service, repository, model e DTO."
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# Crea repo GitHub via API REST
def create_github_repo():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    data = {
        "name": REPO_NAME,
        "private": False,
        "auto_init": False
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"✅ Repository creato: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
    elif response.status_code == 422:
        print("ℹ️ Repo esiste già.")
    else:
        raise Exception(f"❌ Errore nella creazione del repo: {response.status_code}\n{response.text}")

# Inizializza Git se non esiste
def setup_git_repo():
    if not os.path.exists(os.path.join(PROJECT_PATH, ".git")):
        subprocess.run(["git", "init"], cwd=PROJECT_PATH)
        subprocess.run(["git", "branch", "-m", "main"], cwd=PROJECT_PATH)
        subprocess.run(["git", "remote", "add", "origin",
                        f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"], cwd=PROJECT_PATH)
        print("✅ Inizializzato repository locale.")

# Commit & Push
def commit_and_push():
    subprocess.run(["git", "add", "."], cwd=PROJECT_PATH)

    msg = generate_commit_message()
    subprocess.run(["git", "commit", "-m", msg], cwd=PROJECT_PATH)
 
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=PROJECT_PATH)
    print("🚀 Codice pushato su GitHub.")

if __name__ == "__main__":
    create_github_repo()
    setup_git_repo()
    commit_and_push()
