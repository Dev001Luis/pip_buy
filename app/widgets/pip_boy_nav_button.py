from kivy.uix.button import Button
from kivy.graphics import Color, Line
from app.core.theme import theme


class PipBoyNavButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)

        self.color = theme.text
        self.font_name = theme.font

        self.bind(pos=self.update_canvas, size=self.update_canvas)

        with self.canvas.before:
            Color(*theme.primary)
            self.frame = Line(
                rectangle=(self.x, self.y, self.width, self.height), width=1
            )

    def update_canvas(self, *args):
        self.frame.rectangle = (self.x, self.y, self.width, self.height)

    def set_active(self, active):

        if active:
            self.frame.width = 3
        else:
            self.frame.width = 1
