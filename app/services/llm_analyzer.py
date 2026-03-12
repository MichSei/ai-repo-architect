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