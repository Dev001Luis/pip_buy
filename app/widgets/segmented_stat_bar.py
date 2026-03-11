from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from app.core.theme import theme


class SegmentedBar(Widget):

    def __init__(self, max_value=10, value=5, **kwargs):
        super().__init__(**kwargs)

        self.max_value = max_value
        self.value = value

        self.bind(pos=self.update_bar, size=self.update_bar)

    def update_bar(self, *args):

        self.canvas.clear()

        segment_width = self.width / self.max_value
        segment_height = self.height

        with self.canvas:

            for i in range(self.max_value):

                if i < self.value:
                    Color(*theme.text)
                else:
                    Color(0.1, 0.2, 0.1, 1)

                Rectangle(
                    pos=(self.x + i * segment_width, self.y),
                    size=(segment_width - 4, segment_height),
                )


class SegmentedStatBar(BoxLayout):

    def __init__(self, label, value=5, max_value=10, **kwargs):
        super().__init__(orientation="horizontal", **kwargs)

        self.size_hint_y = None
        self.height = 40
        self.spacing = 10

        self.label = Label(
            text=label,
            font_name=theme.font,
            font_size=20,
            size_hint_x=0.2,
            color=theme.text,
        )

        self.bar = SegmentedBar(value=value, max_value=max_value, size_hint_x=0.8)

        self.add_widget(self.label)
        self.add_widget(self.bar)

    def set_value(self, value):
        self.bar.value = value
        self.bar.update_bar()
