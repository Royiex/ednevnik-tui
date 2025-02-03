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


def get_grades():
    try:
        data = json.loads(Start())
        grades_data = {}
        
        for subject, details in data.get("classes", {}).items():
            grades_list = []
            for index, (grade_key, grade_info) in enumerate(details.get("grades", {}).items()):
                grades_list.append((index, grade_info.get("date", "N/A"), grade_info))
            
            grades_data[subject] = {
                "teacher_name": details.get("teacher_name", "Unknown"),
                "average_grade": details.get("average_grade", "N/A"),
                "grades": grades_list
            }
        
        return grades_data
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
