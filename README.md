# AI GitHub Repository Analyzer

An AI-powered tool that analyzes GitHub repositories and generates architecture insights using a local LLM.

## Features

- Clone and analyze any GitHub repository
- Detect programming languages
- Detect frameworks and technologies
- Identify architecture layers
- Generate architecture summaries with AI
- Generate architecture diagrams
- Visual web interface for analysis

## Tech Stack

Backend:
- FastAPI
- Python

AI:
- Ollama
- Llama3

Visualization:
- Mermaid diagrams

## Demo

### Web Interface

![UI Demo](docs/screenshots/ui-demo.png)

### Example Output

Architecture summary and diagram generated automatically from a repository.

## How It Works

1. User submits a GitHub repository URL
2. The repo is cloned locally
3. Static analysis extracts:
   - languages
   - technologies
   - architecture layers
4. A local LLM generates:
   - architecture summary
   - architecture diagram
5. Results are displayed in the UI

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt