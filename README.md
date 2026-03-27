# AI Repository Analyzer

A tool that takes a GitHub repository and gives a quick overview of how the project is structured.

It clones the repo locally, scans the code, and uses a local model to explain the architecture, generate a diagram, and answer questions about the codebase.

---

## What it does

* Clone any public GitHub repository
* Detect programming languages and frameworks
* Identify common architecture layers (e.g. routers, services, models)
* Generate a short architecture summary
* Create a simple architecture diagram (Mermaid)
* Let you ask questions about the codebase
* Show which files answers are based on

---

## Tech stack

* Backend: FastAPI
* Local LLM: Ollama (Llama 3)
* Embeddings: sentence-transformers
* Vector search: ChromaDB
* UI: Jinja templates + Mermaid

---

## How it works

1. Enter a GitHub repo URL
2. The repo is cloned locally
3. Files are scanned and analyzed
4. Code is split into chunks and embedded
5. A local model generates:

   * architecture summary
   * architecture diagram
6. You can ask questions about the repo

   * relevant code is retrieved
   * the model generates an answer with sources

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Start Ollama

```bash
ollama serve
```

Make sure you have the model installed:

```bash
ollama run llama3
```

---

### 3. Run the backend

```bash
uvicorn app.main:app --reload
```

---

### 4. Open the app

```text
http://127.0.0.1:8000/ui
```

---

## Notes

* First analysis of a repo is slower (indexing + embeddings)
* After that, results are cached and much faster
* Everything runs locally (no external API required)

---

## Limitations

* Best support for Python projects (for now)
* Large repos may take longer to index
* Architecture diagrams are simplified

---

## Future ideas

* Better support for non-Python repos
* Persistent cache (so indexing survives restarts)
* More accurate dependency graphs
* Improved diagram generation
