from kivy_garden.mapview import MapMarker
from kivy.graphics import Color, Ellipse


class PlayerMarker(MapMarker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # draw a green circle marker
        with self.canvas:
            Color(0, 1, 0, 1)
            self.circle = Ellipse(size=(20, 20))

        self.bind(pos=self.update_circle)

    def update_circle(self, *args):
        self.circle.pos = (self.center_x - 10, self.center_y - 10)
