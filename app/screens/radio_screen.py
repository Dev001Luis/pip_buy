from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class RadioScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="RADIO SCREEN", font_size=40)

        self.add_widget(label)
