from pathlib import Path
import json
import random

from kivy.core.audio import SoundLoader
from kivy.clock import Clock


DATA_FILE = Path("app/data/radio_stations.json")
MUSIC_PATH = Path("app/assets/sounds/music")
STATIC_SOUND = "app/assets/sounds/radio_static.mp3"


class RadioManager:

    def __init__(self):

        self.stations = []
        self.current_station = None
        self.current_track_index = 0
        self.current_sound = None

        self.static_sound = SoundLoader.load(STATIC_SOUND)
        self.radio_on = False

        self.load_stations()

    # ------------------------

    def load_stations(self):

        if not DATA_FILE.exists():
            return

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        for station in data["stations"]:

            folder = MUSIC_PATH / station["folder"]

            tracks = list(folder.glob("*.ogg"))

            random.shuffle(tracks)

            self.stations.append({"name": station["name"], "tracks": tracks})

    # ------------------------

    def play_station(self, index):

        self.radio_on = True

        self.current_station = self.stations[index]
        self.current_track_index = 0

        self.play_current()

    # ------------------------

    def play_current(self):

        tracks = self.current_station["tracks"]

        if not tracks:
            return

        track_path = tracks[self.current_track_index]

        self.play_with_static(track_path)

    # ------------------------

    def play_with_static(self, track_path):

        if self.static_sound:
            self.static_sound.play()

        Clock.schedule_once(lambda dt: self._play_track(track_path), 0.2)

    # ------------------------

    def _play_track(self, track_path):

        if self.current_sound:
            self.current_sound.stop()

        self.current_sound = SoundLoader.load(str(track_path))

        if self.current_sound:

            self.current_sound.play()

            self.current_sound.bind(on_stop=self._on_track_end)

    # ------------------------

    def pause(self):

        if self.current_sound:
            self.current_sound.stop()

    # ------------------------

    def resume(self):

        if self.current_sound:
            self.current_sound.play()

    # ------------------------

    def stop(self):

        self.radio_on = False

        if self.current_sound:
            self.current_sound.unbind(on_stop=self._on_track_end)
            self.current_sound.stop()

    # ------------------------

    def _on_track_end(self, *args):

        if not self.radio_on:
            return

        self.next_track()

    # ------------------------

    def next_track(self):

        if not self.current_station:
            return

        tracks = self.current_station["tracks"]

        if not tracks:
            return

        self.current_track_index = (self.current_track_index + 1) % len(tracks)

        self.play_current()

    # ------------------------

    def previous_track(self):

        if not self.current_station:
            return

        tracks = self.current_station["tracks"]

        if not tracks:
            return

        self.current_track_index = (self.current_track_index - 1) % len(tracks)

        self.play_current()


radio_manager = RadioManager()
