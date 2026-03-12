import os

# directories we ignore
IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build",
    ".idea",
    ".vscode"
}

# file extensions we care about
CODE_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".java",
    ".go",
    ".rs",
    ".cpp",
    ".c",
    ".cs",
    ".rb"
}


def get_repo_structure(repo_path: str):

    structure = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:

            file_path = os.path.join(root, file)

            structure.append(file_path)

    return structure


def get_code_files(repo_path: str):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:

            ext = os.path.splitext(file)[1]

            if ext in CODE_EXTENSIONS:

                code_files.append(os.path.join(root, file))

    return code_files

def detect_languages(code_files):

    language_map = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".go": "Go",
        ".rs": "Rust",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".rb": "Ruby"
    }

    detected = set()

    for file in code_files:

        ext = os.path.splitext(file)[1]

        if ext in language_map:
            detected.add(language_map[ext])

    return list(detected)

def detect_technologies(repo_path: str):

    technologies = set()

    requirements = os.path.join(repo_path, "requirements.txt")
    pyproject = os.path.join(repo_path, "pyproject.toml")

    if os.path.exists(requirements):

        with open(requirements, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()

            if "fastapi" in content:
                technologies.add("FastAPI")

            if "django" in content:
                technologies.add("Django")

            if "flask" in content:
                technologies.add("Flask")

            if "sqlalchemy" in content:
                technologies.add("SQLAlchemy")

    if os.path.exists(pyproject):

        with open(pyproject, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()

            if "fastapi" in content:
                technologies.add("FastAPI")

            if "django" in content:
                technologies.add("Django")

    package_json = os.path.join(repo_path, "package.json")

    if os.path.exists(package_json):

        with open(package_json, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()

            if "react" in content:
                technologies.add("React")

            if "next" in content:
                technologies.add("Next.js")

            if "vue" in content:
                technologies.add("Vue")

    dockerfile = os.path.join(repo_path, "Dockerfile")

    if os.path.exists(dockerfile):
        technologies.add("Docker")

    return list(technologies)