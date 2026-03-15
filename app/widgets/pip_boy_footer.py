from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from app.core.theme import theme

from datetime import datetime
from kivy.clock import Clock


class PipBoyFooter(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint_y = None
        self.height = 40
        self.padding = 10
        self.spacing = 30
        self.width = 0.70

        with self.canvas.before:
            Color(*theme.inverse_green)
            self.bg = Rectangle()

        self.bind(pos=self.update_rect, size=self.update_rect)

        self.left_label = Label(
            text="HP 81/100", color=theme.text, font_name=theme.font
        )

        self.center_label = Label(
            text="LEVEL 32", color=theme.text, font_name=theme.font
        )

        self.right_label = Label(text="", color=theme.text, font_name=theme.font)
        Clock.schedule_interval(self.update_clock, 0.60)

        self.add_widget(self.left_label)
        self.add_widget(self.center_label)
        self.add_widget(self.right_label)

    def update_clock(self, dt):

        now = datetime.now()

        time_string = now.strftime("%d.%m.%Y  %H:%M")

        self.right_label.text = time_string

    def update_rect(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
