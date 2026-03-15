from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from app.core.theme import theme


class PipBoyScreen(BoxLayout):

    def __init__(self, title="", **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # IMPORTANT: this makes the widget fill the entire Screen
        self.size_hint = (1, 1)
        # HEADER
        # self.header = Label(
        #     text=title,
        #     size_hint_y=None,
        #     height=50,
        #     font_name=theme.font,
        #     font_size=24,
        #     color=theme.text,
        # )
        # self.add_widget(self.header)

        # CONTENT AREA (all screens inject their layout here)
        self.content = BoxLayout(orientation="vertical", size_hint_y=1)
        self.add_widget(self.content)
        self.content.padding = [40, 20]
        self.content.spacing = 10

        # FOOTER
        # self.footer = Label(
        #     text="PIP-BOY 3000 MK IV",
        #     size_hint_y=None,
        #     height=40,
        #     font_name=theme.font,
        #     font_size=16,
        #     color=theme.text,
        # )
        # self.add_widget(self.footer)
