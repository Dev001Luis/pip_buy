from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line


class CRTOverlay(Widget):
    """
    Draws simple horizontal scanlines over a screen to simulate CRT
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.draw_lines, pos=self.draw_lines)

    def draw_lines(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0, 0.05)  # faint green lines
            spacing = 4
            for y in range(0, int(self.height), spacing):
                Line(points=[0, y, self.width, y], width=1)
