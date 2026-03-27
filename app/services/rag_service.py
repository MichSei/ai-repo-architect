import ollama
from app.services.embedding_service import search_code


def answer_repo_question(question: str):

    results = search_code(question)

    context = "\n\n".join([r["code"] for r in results])

    sources = list(set([r["path"] for r in results]))

    prompt = f"""
You are an expert software engineer.

A user asked a question about a codebase.

Question:
{question}

Relevant code snippets:
{context}

Explain the answer clearly based on the code.
If possible mention file names or components.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    return answer, sources