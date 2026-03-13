from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from app.screens.stat_screen import StatScreen
from app.screens.inventory_screen import InventoryScreen
from app.screens.data_screen import DataScreen
from app.screens.map_screen import MapScreen
from app.screens.radio_screen import RadioScreen
from app.screens.boot_screen import BootScreen

from app.widgets.navbar import NavBar
from app.widgets.ctr_overlay import CRTOverlay
from app.widgets.screen_glow import ScreenGlow


Config.set("graphics", "width", "900")
Config.set("graphics", "height", "500")
Config.set("graphics", "resizable", "0")


class PipBoyApp(App):

    def build(self):

        # ROOT (allows overlay layering)
        root = FloatLayout()

        # MAIN UI LAYOUT
        main_layout = BoxLayout(orientation="vertical", size_hint=(1, 1))

        # SCREEN MANAGER
        screen_manager = ScreenManager(size_hint=(1, 1))

        screen_manager.add_widget(BootScreen(name="boot"))
        screen_manager.add_widget(StatScreen(name="stat"))
        screen_manager.add_widget(InventoryScreen(name="inv"))
        screen_manager.add_widget(DataScreen(name="data"))
        screen_manager.add_widget(MapScreen(name="map"))
        screen_manager.add_widget(RadioScreen(name="radio"))

        screen_manager.current = "boot"

        # NAVBAR
        navbar = NavBar(screen_manager)
        navbar.size_hint_y = None
        navbar.height = 60
        navbar.opacity = 0
        navbar.disabled = True

        # BUILD MAIN LAYOUT
        main_layout.add_widget(navbar)
        main_layout.add_widget(screen_manager)

        # ADD MAIN LAYOUT TO ROOT
        root.add_widget(main_layout)

        # ADD SCREEN GLOW EFFECT
        glow = ScreenGlow()
        root.add_widget(glow)

        # CRT OVERLAY (on top of everything)
        overlay = CRTOverlay(size_hint=(1, 1))
        root.add_widget(overlay)

        return root


if __name__ == "__main__":
    PipBoyApp().run()
