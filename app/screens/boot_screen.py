from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.clock import Clock

from app.core.theme import theme
from app.core.sound_manager import sound_manager


class BootScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.boot_lines = [
            "",
            "VAULT-TEC INDUSTRIES",
            "",
            "INITIALIZING PIP-BOY 3000 MK IV...",
            "LOADING SYSTEM FILES...",
            "CHECKING RADIATION LEVELS...",
            "SYNCING VAULT DATABASE...",
            "",
            "WELCOME VAULT DWELLER",
        ]

        self.current_line = 0

        self.label = Label(
            text="",
            font_name=theme.font,
            font_size=22,
            color=theme.text,
            halign="center",
            valign="top",
        )

        self.label.bind(size=self.label.setter("text_size"))

        self.add_widget(self.label)

        Clock.schedule_once(self.start_boot, 0.5)

    def start_boot(self, dt):
        sound_manager.play_opening_beep()
        Clock.schedule_interval(self.print_line, 0.6)

    def print_line(self, dt):

        if self.current_line >= len(self.boot_lines):
            Clock.schedule_once(self.finish_boot, 1)
            return False

        line = self.boot_lines[self.current_line]

        # play terminal sound
        if line.strip():
            sound_manager.play_boot_line()

        self.label.text += line + "\n"

        self.current_line += 1

    def finish_boot(self, dt):
        root = self.manager.parent
        navbar = root.children[1]

        navbar.opacity = 1
        navbar.disabled = False

        self.manager.current = "stat"
