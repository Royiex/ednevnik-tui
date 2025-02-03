from textual.app import App, ComposeResult
from textual.widgets import Footer, TabPane, TabbedContent
from data import get_classes, sanitize_name
# import re

classes_original = get_classes()
classes_sanitized = [sanitize_name(name) for name in classes_original]


class ednevnikTui(App):

    def compose(self) -> ComposeResult:
        yield Footer()
        with TabbedContent():
            for original, sanitized in zip(classes_original, classes_sanitized):
                yield TabPane(original, id=sanitized)


# def main(data):
#     classes_original = data
#     classes_sanitized = [sanitize_name(name) for name in classes_original]
if __name__ == "__main__":
    app = ednevnikTui()
    app.run()
