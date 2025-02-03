import json
import re
import unicodedata
from scraper import Start


def get_classes():
    try:
        data = json.loads(Start())
        # data = f
        classes = []

        for class_obj in data.get("classes", []):
            classes.append(class_obj)
        return classes
    except Exception as e:
        print(f"unexpected error {e}")
        return []

def sanitize_name(name: str) -> str:
    # Normalize Unicode characters (e.g., č -> c, ž -> z)
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    # Replace non-alphanumeric characters with "_"
    return re.sub(r'\W+', '_', name.lower()).strip('_')

# print(get_classes())
