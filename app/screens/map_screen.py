from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView

import geocoder

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.player_marker import PlayerMarker
from app.widgets.quest_marker import QuestMarker
from app.widgets.pipboy_map_filter import PipBoyMapFilter


class MapScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="MAP")

        container = FloatLayout()

        # MAP
        # setted to Lincoln, Lincolnshire for now
        self.map = MapView(zoom=17, lat=53.238701, lon=-0.544168)

        container.add_widget(self.map)

        # Green filter overlay
        container.add_widget(PipBoyMapFilter())

        layout.content.add_widget(container)

        self.add_widget(layout)

        # player marker
        self.player = PlayerMarker(lat=53.238701, lon=-0.544168)

        self.map.add_marker(self.player)

        # example quest marker
        quest = QuestMarker(lat=53.238706, lon=-0.544167)

        self.map.add_marker(quest)

        # self.detect_location() # TODO to uncomment when global VPN is off

    def detect_location(self):

        g = geocoder.ip("me")

        if g.ok:
            lat, lon = g.latlng

            self.map.center_on(lat, lon)

            self.player.lat = lat
            self.player.lon = lon
