from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs
from app.core.theme import theme
from app.core.inventory_manager import inventory_manager


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="INV")

        self.content_layout = BoxLayout(orientation="vertical")

        tabs = SegmentedTabs(
            tabs=["LANGUAGES", "FRAMEWORKS", "SOFTWARES"], callback=self.switch_tab
        )

        self.display = Label(
            text="Select a category",
            font_name=theme.font,
            font_size=22,
            color=theme.text,
        )

        self.content_layout.add_widget(tabs)
        self.content_layout.add_widget(self.display)

        layout.content.add_widget(self.content_layout)

        self.add_widget(layout)

    def switch_tab(self, tab_name):

        mapping = {
            "LANGUAGES": "languages",
            "FRAMEWORKS": "frameworks",
            "SOFTWARES": "softwares",
        }

        category_key = mapping.get(tab_name)
        items = inventory_manager.get_category(category_key)

        if items:
            self.display.text = "\n".join(items)
        else:
            self.display.text = "No items yet."
