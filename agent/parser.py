import os
import re

def parse_output_to_files():
    for file in os.listdir("generated_projects"):
        if not file.startswith("output_step_"):
            continue

        full_path = os.path.join("generated_projects", file)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 🔧 Rimuove blocchi markdown tipo ```java, ```xml, ``` ecc.
        content = re.sub(r"```[a-z]*\n?", "", content, flags=re.IGNORECASE)
        content = content.replace("```", "").strip()

        # 📎 Match tipo: --- path/nomefile.ext --- \n <codice>
        pattern = r"---\s*(.*?)\s*---\n(.+?)(?=(?:---|$))"
        matches = re.findall(pattern, content, re.DOTALL)

        if not matches:
            print(f"⚠️ Nessun file valido in: {file}")
            continue

        for relative_path, code in matches:
            relative_path = relative_path.strip()

            # 🔒 Skip file non validi
            if not any(relative_path.endswith(ext) for ext in [".java", ".xml", ".properties", ".yml", ".json", ".txt"]):
                print(f"⛔ Ignorato path non valido: {relative_path}")
                continue

            # 📁 Percorso finale con separatori OS-friendly
            filepath = os.path.join("generated_projects", "project", relative_path.replace("/", os.sep))
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, "w", encoding="utf-8") as out:
                out.write(code.strip())
                print(f"✅ Creato: {filepath}")

if __name__ == "__main__":
    parse_output_to_files()
