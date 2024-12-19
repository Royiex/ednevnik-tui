from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container, Grid, Horizontal
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """
    def render(self) -> RenderResult:
        return "Hello, [b]World[/b]!"

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class Maininfo(Placeholder):
    DEFAULT_CSS = """
    Maininfo {
        width: 1fr;
        height: 1fr;
    }
    """

class Row(Horizontal):
    DEFAULT_CSS = """
    Row {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Maininfo(id="main1")
        yield Maininfo(id="main2")

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        with Grid():
            yield Row()
            yield Row()


class Layout(App):
    def on_mount(self) -> None:
        self.push_screen(MainScreen())

    # def on_ready(self) -> None:
    #     self.update_clock()
    #     self.set_interval(1, self.update_clock)

    # def update_clock(self) -> None:
    #     clock = datetime.now().time()
    #     self.query_one(Digits).update(f"{clock:%T}")



if __name__ == "__main__":
    Layout().run()
