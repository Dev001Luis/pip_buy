from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import random

from app.core.theme import theme
from app.core.radio_manager import radio_manager


class RadioSignal(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bars = []
        self.bar_count = 16

        with self.canvas:

            Color(*theme.primary)

            for _ in range(self.bar_count):

                rect = Rectangle(pos=(0, 0), size=(10, 10))
                self.bars.append(rect)

        Clock.schedule_interval(self.animate, 0.1)

    def animate(self, dt):

        if not radio_manager.radio_on:
            return

        width = self.width / self.bar_count

        for i, bar in enumerate(self.bars):

            height = random.randint(10, int(self.height))

            bar.pos = (self.x + i * width, self.y)
            bar.size = (width * 0.8, height)
