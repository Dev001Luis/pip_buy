from kivy_garden.mapview import MapMarker
from kivy.graphics import Color, Line


class QuestMarker(MapMarker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)

            self.cross = Line(
                points=[
                    self.center_x - 10,
                    self.center_y,
                    self.center_x + 10,
                    self.center_y,
                    self.center_x,
                    self.center_y - 10,
                    self.center_x,
                    self.center_y + 10,
                ],
                width=2,
            )

        self.bind(pos=self.update_cross)

    def update_cross(self, *args):

        cx = self.center_x
        cy = self.center_y

        self.cross.points = [
            cx - 10,
            cy,
            cx + 10,
            cy,
            cx,
            cy - 10,
            cx,
            cy + 10,
        ]
