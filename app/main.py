from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.services.repo_cloner import clone_repository
from app.services.repo_analyzer import (
    get_repo_structure,
    get_code_files,
    detect_languages,
    detect_technologies
)
from app.services.llm_analyzer import (
    generate_architecture_summary,
    generate_architecture_diagram
)
from app.services.architecture_detector import detect_architecture_layers

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

class RepoRequest(BaseModel):
    repo_url: str

@app.get("/")
def root():
    return {"message": "AI Repo Architect is running"}

@app.get("/ui", response_class=HTMLResponse)
def ui_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/analyze", response_class=HTMLResponse)
def analyze_from_form(request: Request, repo_url: str = Form(...)):
    repo_path = clone_repository(repo_url)

    structure = get_repo_structure(repo_path)
    code_files = get_code_files(repo_path)
    languages = detect_languages(code_files)
    technologies = detect_technologies(repo_path)
    layers = detect_architecture_layers(repo_path)

    summary = generate_architecture_summary(code_files, languages, technologies)
    diagram = generate_architecture_diagram(languages, technologies, layers)

    result = {
        "repo_path": repo_path,
        "total_files": len(structure),
        "code_files": len(code_files),
        "languages_detected": languages,
        "technologies_detected": technologies,
        "architecture_layers": layers,
        "architecture_summary": summary,
        "architecture_diagram": diagram,
        "sample_files": code_files[:20],
    }

    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@app.post("/analyze-repo")
def analyze_repo(request: RepoRequest):

    repo_path = clone_repository(request.repo_url)

    structure = get_repo_structure(repo_path)

    code_files = get_code_files(repo_path)

    languages = detect_languages(code_files)

    technologies = detect_technologies(repo_path)

    summary = generate_architecture_summary(code_files, languages, technologies)

    layers = detect_architecture_layers(repo_path)

    diagram = generate_architecture_diagram(languages, technologies, layers)

  

    return {
    "repo_path": repo_path,
    "total_files": len(structure),
    "code_files": len(code_files),
    "languages_detected": languages,
    "technologies_detected": technologies,
    "architecture_summary": summary,
    "architecture_diagram": diagram,
    "sample_files": code_files[:20],
    "architecture_layers": layers
}