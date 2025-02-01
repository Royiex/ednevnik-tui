import json
import re
import unicodedata


def get_classes():
    with open("main.json") as f:
        data = json.load(f)

    classes = []

    for class_obj in data.get("classes", []):
        classes.append(class_obj)
    return classes


def sanitize_name(name: str) -> str:
    # Normalize Unicode characters (e.g., č -> c, ž -> z)
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    # Replace non-alphanumeric characters with "_"
    return re.sub(r'\W+', '_', name.lower()).strip('_')
