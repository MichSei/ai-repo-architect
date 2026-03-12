from fastapi import FastAPI
from pydantic import BaseModel

from app.services.repo_cloner import clone_repository
from app.services.repo_analyzer import get_repo_structure

app = FastAPI()


class RepoRequest(BaseModel):
    repo_url: str


@app.get("/")
def root():
    return {"message": "AI Repo Architect is running"}


@app.post("/analyze-repo")
def analyze_repo(request: RepoRequest):

    repo_path = clone_repository(request.repo_url)

    structure = get_repo_structure(repo_path)

    return {
        "repo_path": repo_path,
        "file_count": len(structure),
        "files": structure[:50]
    }