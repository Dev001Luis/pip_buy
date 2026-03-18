from pathlib import Path
import json
import random

from kivy.core.audio import SoundLoader
from kivy.clock import Clock


import os
from kivy.app import App


class RadioManager:
    def __init__(self):
        # Dynamically find the app directory
        base = App.get_running_app().directory

        self.data_file = os.path.join(base, "app", "data", "radio_stations.json")
        self.music_path = Path(os.path.join(base, "app", "assets", "sounds", "music"))
        self.static_path = os.path.join(
            base, "app", "assets", "sounds", "radio_static.mp3"
        )

        self.stations = []
        # ... rest of init ...
        self.static_sound = SoundLoader.load(self.static_path)
        self.load_stations()

    def load_stations(self):
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for station in data["stations"]:
            folder = self.music_path / station["folder"]
            # Note: Android glob is case sensitive, ensure extensions are .ogg
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
            self.ignore_stop_event = True
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

        if self.ignore_stop_event:
            self.ignore_stop_event = False
            return

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

    def get_now_playing(self):

        if not self.current_station:
            return None, None

        station_name = self.current_station["name"]

        tracks = self.current_station["tracks"]

        if not tracks:
            return station_name, None

        track_path = tracks[self.current_track_index]

        song_name = track_path.stem.replace("_", " ").title()

        return station_name, song_name


radio_manager = RadioManager()
