from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs
from app.core.theme import theme


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="INV")

        self.content_layout = BoxLayout(orientation="vertical")

        tabs = SegmentedTabs(
            tabs=["LANGUAGES", "FRAMEWORKS", "SOFTWARES"], callback=self.switch_tab
        )

        self.display = Label(
            text="Select a category",
            font_name=theme.font,
            font_size=22,
            color=theme.text,
        )

        self.content_layout.add_widget(tabs)
        self.content_layout.add_widget(self.display)

        layout.content.add_widget(self.content_layout)

        self.add_widget(layout)

    def switch_tab(self, tab_name):

        if tab_name == "LANGUAGES":
            self.display.text = "Python\nJavaScript\nSQL"

        elif tab_name == "FRAMEWORKS":
            self.display.text = "Flask\nFastAPI\nVue"

        elif tab_name == "SOFTWARES":
            self.display.text = "Git\nDocker\nLinux"
