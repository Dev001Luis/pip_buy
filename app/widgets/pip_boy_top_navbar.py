from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from app.core.theme import theme


class PipBoyTopNav(BoxLayout):

    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 60
        self.spacing = 40
        self.padding = [80, 10]

        self.sm = screen_manager

        self.tabs = {}
        self.active = "stat"

        names = [
            ("STAT", "stat"),
            ("INV", "inv"),
            ("DATA", "data"),
            ("MAP", "map"),
            ("RADIO", "radio"),
        ]

        for text, name in names:

            lbl = Label(
                text=text,
                color=theme.text,
                font_name=theme.font,
                size_hint=(None, 1),
                width=90,
            )

            lbl.bind(
                on_touch_down=lambda inst, touch, n=name: self._click(inst, touch, n)
            )

            self.tabs[name] = lbl
            self.add_widget(lbl)

        with self.canvas.after:
            Color(*theme.primary)
            self.line_left = Line(width=1)
            self.line_right = Line(width=1)

        self.bind(pos=self.update_line, size=self.update_line)

    def _click(self, widget, touch, screen):

        if widget.collide_point(*touch.pos):
            self.sm.current = screen
            self.active = screen
            self.update_line()

    def update_line(self, *args):

        active_widget = self.tabs[self.active]

        x1 = self.x
        x2 = active_widget.x - 10
        x3 = active_widget.right + 10
        x4 = self.right

        y = self.y + 5

        self.line_left.points = [x1, y, x2, y]
        self.line_right.points = [x3, y, x4, y]
