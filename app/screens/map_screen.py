from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class MapScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="MAP SCREEN", font_size=40)

        self.add_widget(label)
