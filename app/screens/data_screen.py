from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from app.widgets.pipboy_layout import PipBoyLayout
from app.core.theme import theme


class DataScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyLayout()

        label = Label(text="DATA", font_name=theme.font, font_size=40, color=theme.text)

        layout.add_widget(label)

        self.add_widget(layout)
