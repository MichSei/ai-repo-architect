import ollama


def generate_architecture_summary(code_files, languages, technologies):

    files_sample = "\n".join(code_files[:40])

    prompt = f"""
You are a senior software architect.

Analyze this GitHub repository.

Languages:
{languages}

Technologies:
{technologies}

Example files:
{files_sample}

Explain:

1. What type of project this is
2. The likely architecture
3. The major components

Provide a short architecture summary.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


def generate_architecture_diagram(languages, technologies):

    prompt = f"""
You are a software architect.

Based on this project information:

Languages:
{languages}

Technologies:
{technologies}

Generate a Mermaid architecture diagram.

IMPORTANT RULES:
- Output ONLY Mermaid code
- Do NOT explain anything
- Do NOT include markdown
- Start with: graph TD

Example output:

graph TD
Client --> API
API --> Services
Services --> Database
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    diagram = response["message"]["content"]

    diagram = diagram.replace("```mermaid", "").replace("```", "")

    return diagram.strip()