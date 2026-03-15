import os
import ast


def build_module_graph(repo_path):

    graph = []

    for root, _, files in os.walk(repo_path):

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root, file)

            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    tree = ast.parse(f.read())

                module_name = os.path.basename(root)

                for node in ast.walk(tree):

                    if isinstance(node, ast.ImportFrom):

                        if node.module:
                            graph.append({
                                "from": module_name,
                                "to": node.module.split(".")[0]
                            })

            except:
                continue

    return graph