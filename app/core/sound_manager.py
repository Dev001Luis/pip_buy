from kivy.core.audio import SoundLoader


class SoundManager:

    def __init__(self):
        self.click = SoundLoader.load("app/assets/sounds/tab_change.mp3")
        self.boot = SoundLoader.load("app/assets/sounds/tab_change.mp3")
        self.opening_beep = SoundLoader.load("app/assets/sounds/opening_beep.mp3")

    def play_click(self):
        if self.click:
            self.click.stop()
            self.click.play()

    def play_boot_line(self):
        if self.boot:
            self.boot.stop()
            self.boot.play()

    def play_opening_beep(self):
        self.opening_beep.stop()
        self.opening_beep.play()


sound_manager = SoundManager()
