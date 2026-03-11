from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

from app.core.theme import theme


class StatBar(BoxLayout):

    def __init__(self, label, max_value=100, value=50, **kwargs):
        super().__init__(orientation="horizontal", **kwargs)

        self.size_hint_y = None
        self.height = 40
        self.spacing = 10

        # Label (HP / AP / RAD)
        self.stat_label = Label(
            text=label,
            font_name=theme.font,
            font_size=20,
            size_hint_x=0.2,
            color=theme.text,
        )

        # Progress bar
        self.bar = ProgressBar(max=max_value, value=value, size_hint_x=0.8)

        self.add_widget(self.stat_label)
        self.add_widget(self.bar)

    def set_value(self, value):
        self.bar.value = value
