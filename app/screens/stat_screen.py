from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from app.widgets.character_panel import CharacterPanel

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs

# from app.widgets.stat_bar import StatBar
from app.widgets.segmented_stat_bar import SegmentedStatBar

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

        # Scrollable stat list
        scroll = ScrollView(size_hint=(0.6, 1))

        self.display = GridLayout(cols=1, spacing=15, size_hint_y=None)

        self.display.bind(minimum_height=self.display.setter("height"))

        scroll.add_widget(self.display)

        # Character panel
        character_panel = CharacterPanel(size_hint=(0.4, 1))

        # horizontal container
        display_container = BoxLayout(orientation="horizontal")

        display_container.add_widget(scroll)
        display_container.add_widget(character_panel)

        self.content_layout.add_widget(display_container)
        layout.content.add_widget(self.content_layout)

        self.add_widget(layout)

    def switch_tab(self, tab_name):

        self.display.clear_widgets()

        if tab_name == "STATUS":

            hp = SegmentedStatBar("HP", value=90)
            ap = SegmentedStatBar("AP", value=70)
            rad = SegmentedStatBar("RAD", value=15)

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
                self.display.add_widget(SegmentedStatBar(name, value=value))

        elif tab_name == "PERKS":

            perks = [
                SegmentedStatBar("Clean Code", value=1, max_value=1),
                SegmentedStatBar("Debug Instnct.", value=1, max_value=1),
                SegmentedStatBar("Git Mastery", value=1, max_value=1),
            ]

            for perk in perks:
                self.display.add_widget(perk)
