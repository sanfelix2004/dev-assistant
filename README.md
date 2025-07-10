# 🤖 DevAssistant AI

DevAssistant AI è un agente intelligente scritto in Python, capace di generare automaticamente microservizi backend in Java Spring Boot a partire da una semplice descrizione testuale. Utilizza modelli open-source ospitati su Together.ai (come Mistral e Mixtral) per creare codice strutturato e pronto al deploy, incluso il push automatico su GitHub.

---

## 🚀 Funzionalità principali

- 📥 Input in linguaggio naturale (es: "gestione di un sistema eventi con utenti e prenotazioni")
- 🤖 Generazione completa del microservizio:
  - `Controller.java`
  - `Service.java`
  - `Repository.java`
  - `Model.java`
  - `DTO.java`
  - `pom.xml` e `application.properties`
- 🧠 Commit message generato con AI
- 📂 Parsing e salvataggio automatico in `generated_projects/`
- 🔁 Reset automatico ad ogni generazione
- 🚀 Push automatico su GitHub con creazione dinamica del repository

---

## 🧠 Tecnologie

| Componente       | Tecnologia                          |
|------------------|-------------------------------------|
| Linguaggio       | Python 3.12                         |
| AI/LLM           | Together.ai (`Mixtral`, `Mistral`) |
| Backend target   | Java + Spring Boot                  |
| Librerie Python  | `openai`, `python-dotenv`, `requests` |

---

## 🗂️ Struttura del progetto

