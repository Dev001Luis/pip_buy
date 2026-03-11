from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from app.core.theme import theme


class NavBar(BoxLayout):

    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = 0.1

        self.screen_manager = screen_manager

        self.build_buttons()

    def build_buttons(self):

        buttons = [
            ("STAT", "stat"),
            ("INV", "inv"),
            ("DATA", "data"),
            ("MAP", "map"),
            ("RADIO", "radio"),
        ]

        for text, screen_name in buttons:

            btn = Button(text=text, background_color=theme.primary, color=(0, 0, 0, 1))

            btn.bind(
                on_press=lambda instance, name=screen_name: self.switch_screen(name)
            )

            self.add_widget(btn)

    def switch_screen(self, screen_name):

        self.screen_manager.current = screen_name
