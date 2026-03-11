from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class StatScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="STAT SCREEN", font_size=40)

        self.add_widget(label)
