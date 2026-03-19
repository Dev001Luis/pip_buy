from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from app.core.theme import theme

from datetime import datetime
from kivy.clock import Clock

from app.widgets.radio_controls import RadioControls


class PipBoyFooter(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint_y = None
        self.height = 60
        self.padding = 15
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

        self.controls = RadioControls(size_hint_y=None, height=40)
        controls_container = BoxLayout(
            size_hint_x=0.25,
            size_hint_y=1,
            padding=(0, -15),
        )
        controls_container.add_widget(self.controls)

        self.add_widget(self.left_label)
        self.add_widget(controls_container)
        self.add_widget(self.center_label)
        self.add_widget(self.right_label)

    def update_clock(self, dt):

        now = datetime.now()

        time_string = now.strftime("%d.%m.%Y  %H:%M")

        self.right_label.text = time_string

    def update_rect(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
