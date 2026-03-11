from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from app.core.theme import theme


class PipBoyLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        with self.canvas.before:
            Color(*theme.background)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_bg, pos=self.update_bg)

    def update_bg(self, *args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos
