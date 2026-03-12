import os


def get_repo_structure(repo_path: str):

    structure = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            structure.append(os.path.join(root, file))

    return structure