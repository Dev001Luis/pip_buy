from kivy.uix.boxlayout import BoxLayout
from app.widgets.pip_boy_nav_button import PipBoyNavButton
from app.core.sound_manager import sound_manager


class NavBar(BoxLayout):

    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 60

        self.padding = 10
        self.spacing = 10

        self.sm = screen_manager
        self.buttons = {}

        tabs = [
            ("STAT", "stat"),
            ("INV", "inv"),
            ("DATA", "data"),
            ("MAP", "map"),
            ("RADIO", "radio"),
        ]

        for label, screen in tabs:

            btn = PipBoyNavButton(text=label)

            btn.bind(on_release=lambda inst, s=screen: self.switch_tab(s))

            self.buttons[screen] = btn

            self.add_widget(btn)

        self.set_active("stat")

    def switch_tab(self, screen):

        self.sm.current = screen
        sound_manager.play_click()
        self.set_active(screen)

    def set_active(self, screen):

        for name, btn in self.buttons.items():
            btn.set_active(name == screen)
