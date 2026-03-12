from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class ScreenGlow(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0.1, 1.0, 0.1, 0.05)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
