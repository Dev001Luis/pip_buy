from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class PipBoyMapFilter(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # green phosphor tint
            Color(0.0, 0.9, 0.3, 0.25)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
