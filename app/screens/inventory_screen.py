from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="INVENTORY SCREEN", font_size=40)

        self.add_widget(label)
