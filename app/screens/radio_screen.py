from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.pip_boy_list import PipBoyList

from app.core.radio_manager import radio_manager


class RadioScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="RADIO")

        self.container = BoxLayout(orientation="vertical", padding=30, spacing=20)

        layout.content.add_widget(self.container)

        self.add_widget(layout)

    # -----------------------------

    def on_enter(self):

        self.build_station_list()

    # -----------------------------

    def build_station_list(self):

        self.container.clear_widgets()

        station_names = [station["name"] for station in radio_manager.stations]

        station_names.append("OFF")

        radio_list = PipBoyList(
            station_names, on_select=self.select_station, auto_select=False
        )

        self.container.add_widget(radio_list)

    # -----------------------------

    def select_station(self, station_name):

        if station_name == "OFF":

            radio_manager.stop()
            return

        for i, station in enumerate(radio_manager.stations):

            if station["name"] == station_name:

                radio_manager.play_station(i)
                break
