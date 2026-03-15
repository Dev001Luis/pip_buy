from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from app.core.theme import theme


class PipBoyListItem(Label):

    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)

        self.text = text
        self.font_name = theme.font
        self.color = theme.text
        self.size_hint_y = None
        self.height = 32
        self.halign = "left"
        self.valign = "middle"

        self.selected = False

        with self.canvas.before:
            self.bg_color = Color(0, 0, 0, 0)
            self.bg_rect = Rectangle()

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def set_selected(self, value):

        self.selected = value

        if value:
            self.bg_color.rgba = theme.primary
            self.color = theme.inverse_green
        else:
            self.bg_color.rgba = (0, 0, 0, 0)
            self.color = theme.text
