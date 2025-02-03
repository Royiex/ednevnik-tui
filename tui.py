from textual.app import App, ComposeResult
from textual.widgets import Footer, TabPane, TabbedContent, Label
from data import get_classes, sanitize_name, get_grades
# import re

classes_original = get_classes()
classes_sanitized = [sanitize_name(name) for name in classes_original]
grades_data = get_grades()


class ednevnikTui(App):

    def compose(self) -> ComposeResult:
        yield Footer()
        with TabbedContent():
            for original, sanitized in zip(classes_original, classes_sanitized):
                with TabPane(original, id=sanitized):
                    if original in grades_data:
                        for index, date, grade_info in grades_data[original]["grades"]:
                            unique_id = f"{sanitized}_{date.replace('.', '_')}_{index}"
                            with TabPane(date, id=unique_id):
                                yield Label(f"Date: {date}")
                                yield Label(f"Grade: {grade_info.get('grade', 'N/A')}")
                                yield Label(f"Description: {grade_info.get('description', 'No description')}\n")


if __name__ == "__main__":
    app = ednevnikTui()
    app.run()
