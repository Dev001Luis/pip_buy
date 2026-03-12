from kivy.core.audio import SoundLoader


class SoundManager:

    def __init__(self):
        self.click = SoundLoader.load("app/assets/sounds/pipboy_click.m4a")

    def play_click(self):
        if self.click:
            self.click.play()


sound_manager = SoundManager()
