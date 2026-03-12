import os

COMMON_LAYERS = [
    "routers",
    "routes",
    "controllers",
    "services",
    "models",
    "schemas",
    "database",
    "db",
    "repositories",
    "core",
]


def detect_architecture_layers(repo_path):

    detected_layers = []

    for root, dirs, files in os.walk(repo_path):

        for d in dirs:

            name = d.lower()

            if name in COMMON_LAYERS and name not in detected_layers:
                detected_layers.append(name)

    return detected_layers