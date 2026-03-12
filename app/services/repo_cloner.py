import os
from git import Repo

REPOS_DIR = "repos"


def clone_repository(repo_url: str):

    if not os.path.exists(REPOS_DIR):
        os.makedirs(REPOS_DIR)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(REPOS_DIR, repo_name)

    if os.path.exists(repo_path):
        return repo_path

    Repo.clone_from(repo_url, repo_path)

    return repo_path