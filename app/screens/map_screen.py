from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy_garden.mapview import MapView
import geocoder

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.player_marker import PlayerMarker
from app.widgets.quest_marker import QuestMarker
from app.widgets.pipboy_map_filter import PipBoyMapFilter


class MapScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Base Pip-Boy layout
        layout = PipBoyScreen(title="MAP")

        # MAIN HORIZONTAL CONTAINER
        main_container = BoxLayout(
            orientation="horizontal", spacing=10, padding=[25, 5, 35, 25], size_hint_y=1
        )

        # -----------------------
        # LEFT PANEL (controls)
        # -----------------------
        left_panel = BoxLayout(
            orientation="vertical", size_hint_x=0.30, spacing=10, padding=[5, 5, 5, 0]
        )

        title = Label(text="SET DEST", size_hint_y=None, height=40)

        self.address_input = TextInput(
            hint_text="Enter address", multiline=False, size_hint_y=None, height=40
        )

        search_button = Button(text="SET MARKER", size_hint_y=None, height=40)

        clear_button = Button(text="CLEAR MARKERS", size_hint_y=None, height=40)

        search_button.bind(on_release=self.search_location)
        clear_button.bind(on_release=self.clear_markers)

        # Add widgets to left panel
        left_panel.add_widget(title)
        left_panel.add_widget(self.address_input)
        left_panel.add_widget(search_button)
        left_panel.add_widget(clear_button)

        # -----------------------
        # RIGHT PANEL (map)
        # -----------------------
        map_container = FloatLayout(size_hint_x=0.70)

        self.map = MapView(
            zoom=17,
            lat=53.238701,
            lon=-0.544168,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )

        map_container.add_widget(self.map)

        # Green monochrome overlay on map only
        pipboy_filter = PipBoyMapFilter(size_hint=(1, 1), pos_hint={"x": 0, "y": 0})
        map_container.add_widget(pipboy_filter)

        # -----------------------
        # ADD PANELS TO MAIN CONTAINER
        # -----------------------
        main_container.add_widget(left_panel)  # left panel
        main_container.add_widget(map_container)  # map on right

        # ADD TO SCREEN CONTENT
        layout.content.add_widget(main_container)
        self.add_widget(layout)

        # -----------------------
        # PLAYER AND QUEST MARKERS
        # -----------------------
        self.player = PlayerMarker(lat=53.238701, lon=-0.544168)
        self.map.add_marker(self.player)

        # Store quest markers here
        self.quest_markers = []

        # Example quest marker
        quest = QuestMarker(lat=53.238706, lon=-0.544167)
        self.map.add_marker(quest)

        # self.detect_location()  # Uncomment for live location
        self.quest_markers.append(quest)

    # -----------------------
    # SEARCH LOCATION
    # -----------------------
    def search_location(self, instance):
        address = self.address_input.text.strip()
        if not address:
            return

        try:
            g = geocoder.osm(address, user_agent="pip-boy-app-dev")
            if g.ok:
                lat, lon = g.latlng
                quest = QuestMarker(lat=lat, lon=lon)
                self.map.add_marker(quest)

                self.quest_markers.append(quest)

                self.map.center_on(lat, lon)
            else:
                print(f"[ERROR] Could not find location: {address}")
        except Exception as e:
            print(f"[ERROR] Geocoder failed: {e}")

    # -----------------------
    # CLEAR MARKERS
    # -----------------------
    def clear_markers(self, instance):
        for marker in self.quest_markers:

            try:
                self.map.remove_marker(marker)
            except Exception:
                pass

        self.quest_markers.clear()  # ciaba

    # -----------------------
    # DETECT LOCATION
    # -----------------------
    def detect_location(self):
        g = geocoder.ip("me")
        if g.ok:
            lat, lon = g.latlng
            self.map.center_on(lat, lon)
            self.player.lat = lat
            self.player.lon = lon


# working
