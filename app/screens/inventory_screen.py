from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs
from app.widgets.pip_boy_list import PipBoyList

from app.core.theme import theme
from app.core.inventory_manager import inventory_manager


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PipBoyScreen(title="INV")

        # MAIN VERTICAL LAYOUT
        self.content_layout = BoxLayout(orientation="vertical")

        # ------------------------
        # TABS
        # ------------------------
        tabs = SegmentedTabs(
            tabs=["ITEMS", "LANGUAGES", "FRAMEWORKS", "SOFTWARES"],
            callback=self.switch_tab,
        )

        tabs.size_hint_y = None
        tabs.height = 50

        self.content_layout.add_widget(tabs)

        # ------------------------
        # MAIN TWO PANEL AREA
        # ------------------------
        self.main_area = BoxLayout(
            orientation="horizontal", spacing=20, padding=(10, 10)
        )

        # LEFT PANEL (LIST)
        self.left_panel = BoxLayout(orientation="vertical", size_hint_x=0.40)

        # ScrollView
        self.scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)

        # List container
        self.list_container = GridLayout(cols=1, spacing=4, size_hint_y=None)

        self.list_container.bind(minimum_height=self.list_container.setter("height"))

        self.scroll.add_widget(self.list_container)

        self.left_panel.add_widget(self.scroll)
        # left_panel = BoxLayout(orientation="vertical", size_hint_x=0.40)

        # RIGHT PANEL (PREVIEW)
        self.right_panel = BoxLayout(
            orientation="vertical", size_hint_x=0.60, spacing=10
        )

        # ------------------------
        # RIGHT PANEL CONTENT
        # ------------------------

        self.item_image = Image(
            source="app/assets/images/items/placeholder.png",
            size_hint_y=0.7,
            # allow_stretch=True,
        )

        self.item_description = Label(
            text="Select an item", font_name=theme.font, color=theme.text, valign="top"
        )

        self.item_description.bind(size=self.item_description.setter("text_size"))

        self.right_panel.add_widget(self.item_image)
        self.right_panel.add_widget(self.item_description)

        # ------------------------
        # ADD PANELS
        # ------------------------

        self.main_area.add_widget(self.left_panel)
        self.main_area.add_widget(self.right_panel)

        self.content_layout.add_widget(self.main_area)

        layout.content.add_widget(self.content_layout)
        self.add_widget(layout)

    # -----------------------------------
    # TAB SWITCH
    # -----------------------------------

    def switch_tab(self, tab_name):

        self.list_container.clear_widgets()

        mapping = {
            "ITEMS": "items",
            "LANGUAGES": "languages",
            "FRAMEWORKS": "frameworks",
            "SOFTWARES": "softwares",
        }

        category_key = mapping.get(tab_name)

        items = inventory_manager.get_category(category_key)

        if not items:
            items = ["No items yet"]

        inventory_list = PipBoyList(items, on_select=self.show_item)

        self.list_container.add_widget(inventory_list)

    # -----------------------------------
    # ITEM PREVIEW
    # -----------------------------------

    def show_item(self, item_name):

        # Placeholder logic (can move to DB later)

        if item_name == "No items yet":

            self.item_image.source = "app/assets/images/items/placeholder.png"

            self.item_description.text = "No items available."

        else:

            image_path = (
                f"app/assets/images/items/{item_name.lower().replace(' ', '_')}.png"
            )

            self.item_image.source = image_path

            self.item_description.text = (
                f"{item_name}\n\n"
                "Item description goes here.\n"
                "You can later load this from a JSON or database."
            )

    # -----------------------------------
    # DEFAULT TAB
    # -----------------------------------

    def on_enter(self):
        self.switch_tab("ITEMS")
