from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from app.screens.stat_screen import StatScreen
from app.screens.inventory_screen import InventoryScreen
from app.screens.data_screen import DataScreen
from app.screens.map_screen import MapScreen
from app.screens.radio_screen import RadioScreen

from kivy.config import Config

Config.set("graphics", "width", "900")
Config.set("graphics", "height", "500")
Config.set("graphics", "resizable", "0")

from app.widgets.navbar import NavBar


class PipBoyApp(App):

    def build(self):

        root = BoxLayout(orientation="vertical")

        screen_manager = ScreenManager()

        screen_manager.add_widget(StatScreen(name="stat"))
        screen_manager.add_widget(InventoryScreen(name="inv"))
        screen_manager.add_widget(DataScreen(name="data"))
        screen_manager.add_widget(MapScreen(name="map"))
        screen_manager.add_widget(RadioScreen(name="radio"))

        navbar = NavBar(screen_manager)

        root.add_widget(navbar)
        root.add_widget(screen_manager)

        return root


if __name__ == "__main__":
    PipBoyApp().run()
