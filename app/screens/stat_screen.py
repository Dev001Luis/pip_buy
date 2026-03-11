from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs
from app.widgets.stat_bar import StatBar

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class StatScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="STAT")

        self.content_layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        tabs = SegmentedTabs(
            tabs=["STATUS", "SPECIAL", "PERKS"], callback=self.switch_tab
        )

        tabs.size_hint_y = None
        tabs.height = 50

        self.content_layout.add_widget(tabs)

        # container for dynamic content
        # self.display = BoxLayout(orientation="vertical", spacing=15)
        scroll = ScrollView(size_hint=(1, 1))

        self.display = GridLayout(cols=1, spacing=15, size_hint_y=None)

        self.display.bind(minimum_height=self.display.setter("height"))

        scroll.add_widget(self.display)

        self.content_layout.add_widget(scroll)

        # self.content_layout.add_widget(self.display)

        layout.content.add_widget(self.content_layout)

        self.add_widget(layout)

    def switch_tab(self, tab_name):

        self.display.clear_widgets()

        if tab_name == "STATUS":

            hp = StatBar("HP", value=90)
            ap = StatBar("AP", value=70)
            rad = StatBar("RAD", value=15)

            self.display.add_widget(hp)
            self.display.add_widget(ap)
            self.display.add_widget(rad)

        elif tab_name == "SPECIAL":

            stats = [
                ("STR", 5),
                ("PER", 7),
                ("END", 6),
                ("CHA", 8),
                ("INT", 9),
                ("AGI", 6),
                ("LCK", 4),
            ]

            for name, value in stats:
                self.display.add_widget(StatBar(name, value=value))

        elif tab_name == "PERKS":

            perks = [
                StatBar("Clean Code", value=1, max_value=1),
                StatBar("Debug Instnct.", value=1, max_value=1),
                StatBar("Git Mastery", value=1, max_value=1),
            ]

            for perk in perks:
                self.display.add_widget(perk)
