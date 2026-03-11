from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from app.widgets.pipboy_screen import PipBoyScreen
from app.core.theme import theme


class StatScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="STAT")

        label = Label(
            text="Player Status Information",
            font_name=theme.font,
            font_size=24,
            color=theme.text,
        )

        layout.content.add_widget(label)

        self.add_widget(layout)
