# 🤖 DevAssistant AI

DevAssistant AI è un agente intelligente scritto in Python, capace di generare automaticamente microservizi backend in Java Spring Boot a partire da una semplice descrizione testuale. Utilizza modelli open-source ospitati su Together.ai (come Mistral e Mixtral) per creare codice strutturato e pronto al deploy, incluso il push automatico su GitHub.

---
Ottimo README! Ora lo completo includendo una sezione "⚙️ Come funziona" che spiega passo passo il funzionamento interno di DevAssistant AI:

⚙️ Come funziona
Il funzionamento dell'assistente è suddiviso in step automatizzati:

1. 🧽 Pulizia del progetto precedente
Alla partenza, la cartella generated_projects/ viene pulita (senza eliminare .git se esistente), così da garantire che ogni generazione parta da zero.

2. 🧾 Input del task in linguaggio naturale
L'utente fornisce una descrizione testuale come ad esempio:

gestione di un sistema di prenotazione eventi

3. 🧠 Scomposizione in sottotask AI
Viene creato un array di prompt mirati per generare separatamente:

il file pom.xml

il file application.properties

il Controller.java

il Service.java

il Repository.java

il Model.java

il DTO.java

Ogni prompt viene processato da un modello open-source (es. Mixtral) su Together.ai e il codice viene salvato in output.

4. 🧩 Parsing e salvataggio file
Il codice generato viene convertito automaticamente in file .java, organizzati secondo la struttura standard Maven (src/main/java/...).

5. 📦 Inizializzazione Git + commit AI
Se non già presente, viene inizializzato un repository Git locale.
Viene generato automaticamente un messaggio di commit descrittivo tramite AI.

6. ☁️ Push automatico su GitHub
Se il repository GitHub non esiste, viene creato tramite API REST.

Viene configurato il remote origin.

Il codice viene pushato direttamente nel branch main.

📎 Requisiti
Python 3.12

Variabili .env settate con:
TOGETHER_API_KEY=...
GITHUB_TOKEN=...
GITHUB_USERNAME=...
