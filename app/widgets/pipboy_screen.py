from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from app.core.theme import theme


class PipBoyScreen(BoxLayout):

    def __init__(self, title="SCREEN", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.header = self.build_header(title)
        self.content = BoxLayout()
        self.footer = self.build_footer()

        self.add_widget(self.header)
        self.add_widget(self.content)
        self.add_widget(self.footer)

    def build_header(self, title):

        header = BoxLayout(size_hint_y=0.15)

        label = Label(text=title, font_name=theme.font, font_size=32, color=theme.text)

        header.add_widget(label)

        return header

    def build_footer(self):

        footer = BoxLayout(size_hint_y=0.1)

        label = Label(
            text="PIP-BOY 3000 MK IV",
            font_name=theme.font,
            font_size=16,
            color=theme.text,
        )

        footer.add_widget(label)

        return footer
