from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class CharacterPanel(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        # keeps image centered
        self.padding = 20

        self.character = Image(
            source="app/assets/images/vault_boy_me.png", size_hint=(1, 1)
        )

        self.add_widget(self.character)
