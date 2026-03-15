import os
import ast


def analyze_python_dependencies(repo_path):

    dependencies = []

    for root, _, files in os.walk(repo_path):

        for file in files:
            if file.endswith(".py"):

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        tree = ast.parse(f.read())

                    for node in ast.walk(tree):

                        if isinstance(node, ast.Import):
                            for name in node.names:
                                dependencies.append(name.name)

                        if isinstance(node, ast.ImportFrom):
                            if node.module:
                                dependencies.append(node.module)

                except:
                    continue

    return list(set(dependencies))