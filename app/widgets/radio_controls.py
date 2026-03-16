from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color

from app.core.radio_manager import radio_manager
from app.core.theme import theme


class IconButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.color = theme.text

    def on_press(self):
        self.color = (0.4, 1, 0.4, 1)

    def on_release(self):
        self.color = theme.text

    pass


class RadioControls(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.spacing = 10
        self.size_hint_y = None
        self.height = 50

        self.prev_btn = IconButton(source="app/assets/icons/radio_prev.png")

        self.play_btn = IconButton(source="app/assets/icons/radio_play.png")

        self.next_btn = IconButton(source="app/assets/icons/radio_next.png")

        self.prev_btn.bind(on_release=self.prev_track)
        self.play_btn.bind(on_release=self.toggle_play)
        self.next_btn.bind(on_release=self.next_track)

        self.add_widget(self.prev_btn)
        self.add_widget(self.play_btn)
        self.add_widget(self.next_btn)

    def prev_track(self, *args):
        radio_manager.previous_track()

    def next_track(self, *args):
        radio_manager.next_track()

    def toggle_play(self, *args):

        if radio_manager.current_sound and radio_manager.current_sound.state == "play":
            radio_manager.pause()
            self.play_btn.source = "app/assets/icons/radio_play.png"
        else:
            radio_manager.resume()
            self.play_btn.source = "app/assets/icons/radio_pause.png"
