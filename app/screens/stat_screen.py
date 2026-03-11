from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs
from app.core.theme import theme


class StatScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="STAT")

        self.content_layout = BoxLayout(orientation="vertical", size_hint_y=1)

        tabs = SegmentedTabs(
            tabs=["STATUS", "SPECIAL", "PERKS"], callback=self.switch_tab
        )

        tabs.size_hint_y = None
        tabs.height = 50

        self.content_layout.add_widget(tabs)

        # placeholder display
        self.display = Label(
            text="Select a STAT category",
            font_name=theme.font,
            font_size=22,
            color=theme.text,
        )

        self.content_layout.add_widget(self.display)

        layout.content.add_widget(self.content_layout)

        self.add_widget(layout)

    def switch_tab(self, tab_name):

        if tab_name == "STATUS":
            self.display.text = "HP  : 100\n" "AP  : 75\n" "RAD : 10"

        elif tab_name == "SPECIAL":
            self.display.text = (
                "STR : 5\n"
                "PER : 7\n"
                "END : 6\n"
                "CHA : 8\n"
                "INT : 9\n"
                "AGI : 6\n"
                "LCK : 4"
            )

        elif tab_name == "PERKS":
            self.display.text = "• Clean Code\n" "• Git Mastery\n" "• Debugger Instinct"
