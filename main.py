import os
import shutil
import re

from agent.code_writer import generate_code
from agent.parser import parse_output_to_files
from push_to_github import create_github_repo, setup_git_repo, commit_and_push

# 🔁 Pulisce la cartella ignorando la cartella .git
def safe_delete_generated_projects():
    folder = "generated_projects"
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except PermissionError:
                    print(f"⛔ Skip file bloccato: {name}")
            for name in dirs:
                path = os.path.join(root, name)
                if ".git" in path:
                    continue
                try:
                    os.rmdir(path)
                except OSError:
                    pass
        print("🧹 Pulizia completata.")

# 📌 Estrae l'entità principale dal task
def extract_entity(task):
    match = re.search(r"gestione (di|dei|del|della|delle)?\s*(\w+)", task.lower())
    if match:
        return match.group(2).capitalize()
        
    return "Entity"

if __name__ == "__main__":
    # 🧼 Pulisci cartella generata
    safe_delete_generated_projects()

    # 📥 Input utente
    task = input("📌 Scrivi il task da generare (es. sistema prenotazioni): ")
    entity = extract_entity(task)

    # 📋 Sottotask da generare
    subtasks = [
        f"Genera SOLO il file pom.xml per un progetto in Java Spring Boot che implementa: {task}",
        f"Genera SOLO il file application.properties per: {task}",
        f"Genera src/main/java/com/example/controller/{entity}Controller.java per: {task}",
        f"Genera src/main/java/com/example/service/{entity}Service.java per: {task}",
        f"Genera src/main/java/com/example/repository/{entity}Repository.java per: {task}",
        f"Genera src/main/java/com/example/model/{entity}.java per: {task}",
        f"Genera src/main/java/com/example/dto/{entity}DTO.java per: {task}"
    ]

    # 🧠 Generazione codice AI
    for i, subtask in enumerate(subtasks):
        print(f"\n🧠 Step {i+1}/{len(subtasks)}: {subtask}")
        generate_code(subtask, i + 1)

    # 📁 Parsing file generati
    print("\n📂 Ora creo la struttura dei file...")
    parse_output_to_files()

    # 🚀 Push automatico su GitHub
    print("\n🚀 Push automatico su GitHub in corso...")
    create_github_repo()
    setup_git_repo()
    commit_and_push()
