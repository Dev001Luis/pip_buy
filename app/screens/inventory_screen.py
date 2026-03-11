from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from app.widgets.pipboy_screen import PipBoyScreen
from app.widgets.segmented_tabs import SegmentedTabs
from app.core.theme import theme
from app.core.inventory_manager import inventory_manager


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Base Pip-Boy layout
        layout = PipBoyScreen(title="INV")

        # Container for tabs + scrollable list
        self.content_layout = BoxLayout(orientation="vertical", size_hint_y=1)

        # Segmented tabs at the top
        tabs = SegmentedTabs(
            tabs=["LANGUAGES", "FRAMEWORKS", "SOFTWARES"], callback=self.switch_tab
        )
        tabs.size_hint_y = None
        tabs.height = 50  # fixed height for tabs
        self.content_layout.add_widget(tabs)

        # Scrollable inventory list
        self.display_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.display_layout.bind(minimum_height=self.display_layout.setter("height"))

        scroll = ScrollView(size_hint_y=1)
        scroll.add_widget(self.display_layout)
        self.content_layout.add_widget(scroll)

        # Selected item index
        self.selected_index = 0

        # Add content layout to PipBoyScreen content (footer stays anchored)
        layout.content.add_widget(self.content_layout)
        self.add_widget(layout)

    def switch_tab(self, tab_name):
        """Update the inventory list when a tab is pressed."""
        self.display_layout.clear_widgets()

        mapping = {
            "LANGUAGES": "languages",
            "FRAMEWORKS": "frameworks",
            "SOFTWARES": "softwares",
        }
        category_key = mapping.get(tab_name)
        items = inventory_manager.get_category(category_key)

        if not items:
            items = ["No items yet."]

        # Populate scrollable list with clickable buttons
        for idx, item in enumerate(items):
            btn = Button(
                text=item,
                font_name=theme.font,
                font_size=22,
                size_hint_y=None,
                height=50,
                background_normal="",
                background_down="",
                background_color=(0, 0, 0, 1),
                color=theme.text,
            )
            # Bind touch/click to select item
            btn.bind(on_release=lambda instance, i=idx: self.on_item_click(i))
            self.display_layout.add_widget(btn)

        # Highlight first item by default
        if items and items != ["No items yet."]:
            self.highlight_item(0)

    def highlight_item(self, index):
        """Add '>' marker to the selected item."""
        children = self.display_layout.children
        for i, btn in enumerate(reversed(children)):
            if i == index:
                btn.text = f"> {btn.text.strip('> ')}"
            else:
                btn.text = btn.text.strip("> ")

    def on_item_click(self, index):
        """Update selection when an item is clicked."""
        self.selected_index = index
        self.highlight_item(index)
