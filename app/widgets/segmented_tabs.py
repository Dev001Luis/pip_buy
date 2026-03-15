from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from app.core.theme import theme

from app.core.sound_manager import sound_manager


class SegmentedTabs(BoxLayout):

    def __init__(self, tabs, callback, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = 0.12

        self.callback = callback
        self.tabs = tabs

        self.build_tabs()

    def build_tabs(self):

        for tab_name in self.tabs:

            btn = Button(
                text=tab_name,
                font_name=theme.font,
                font_size=18,
                background_normal="",
                background_down="",
                background_color=(0, 0, 0, 1),
                color=theme.text,
            )

            btn.bind(on_press=lambda instance, name=tab_name: self.callback(name))

            self.add_widget(btn)

    def on_tab_press(self, tab_name):
        sound_manager.play_click()
        self.callback(tab_name)
