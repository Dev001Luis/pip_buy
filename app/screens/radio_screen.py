from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.widget import Widget

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.pip_boy_list import PipBoyList
from app.widgets.radio_signal import RadioSignal
from app.widgets.radio_controls import RadioControls

from app.core.theme import theme
from app.core.radio_manager import radio_manager


class RadioScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="RADIO")

        # MAIN AREA
        self.main_area = BoxLayout(orientation="horizontal", spacing=20, padding=10)

        # -----------------------
        # LEFT PANEL (stations)
        # -----------------------

        self.left_panel = BoxLayout(orientation="vertical", size_hint_x=0.4)

        # -----------------------
        # RIGHT PANEL (radio UI)
        # -----------------------

        self.right_panel = BoxLayout(
            orientation="vertical", size_hint_x=0.6, spacing=20
        )

        self.signal = RadioSignal(size_hint_y=0.5)

        self.now_playing = Label(
            text="RADIO OFF", font_name=theme.font, color=theme.text, font_size=22
        )
        self.controls = RadioControls()

        self.right_panel.add_widget(self.signal)
        self.right_panel.add_widget(self.now_playing)
        self.right_panel.add_widget(self.controls)

        self.main_area.add_widget(self.left_panel)
        self.main_area.add_widget(self.right_panel)

        layout.content.add_widget(self.main_area)

        Clock.schedule_interval(self.update_now_playing, 0.5)

        self.add_widget(layout)

    def on_enter(self):
        radio_manager._setup_paths()
        self.build_station_list()

    def build_station_list(self):

        self.left_panel.clear_widgets()

        station_names = [station["name"] for station in radio_manager.stations]

        station_names.append("OFF")

        radio_list = PipBoyList(
            station_names, on_select=self.select_station, auto_select=False
        )

        radio_list.size_hint_y = None

        self.left_panel.add_widget(radio_list)

        # Spacer pushes stations to the top
        self.left_panel.add_widget(Widget())

    def select_station(self, station_name):

        if station_name == "OFF":
            radio_manager.stop()
            self.now_playing.text = "RADIO OFF"
            return

        for i, station in enumerate(radio_manager.stations):

            if station["name"] == station_name:

                radio_manager.play_station(i)

                self.now_playing.text = f"Playing: {station_name}"
                break

    def update_now_playing(self, dt):
        radio_manager._setup_paths()
        station, song = radio_manager.get_now_playing()

        if not station:
            self.now_playing.text = "RADIO OFF"
            return

        if song:
            self.now_playing.text = f"{station}\n{song}"
        else:
            self.now_playing.text = station
