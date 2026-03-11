from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class DataScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="DATA SCREEN", font_size=40)

        self.add_widget(label)
