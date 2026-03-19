import json
import os
from kivy.app import App
from pathlib import Path


import os
from kivy.app import App
from kivy.utils import platform


class InventoryManager:
    def __init__(self):
        self.base = None
        self.data = {}  # Initialize with an empty dictionary!
        self.data_file = None

    def _setup_paths(self):
        """Lazy load the paths and the JSON data."""
        if self.base is not None:
            return  # Already loaded

        app = App.get_running_app()
        if app:
            self.base = app.directory
        else:
            self.base = os.path.dirname(os.path.abspath(__file__))

        self.data_file = os.path.join(self.base, "app", "data", "dev_inventory.json")
        print(f"DEBUG: Looking for Inventory JSON at: {self.data_file}")
        print(f"DEBUG: Does it exist? {os.path.exists(self.data_file)}")
        self._load_data_internal()

    def _load_data_internal(self):
        """Actually read the JSON."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def get_item_names(self, category):
        # 1. ALWAYS ensure setup is run before accessing self.data
        self._setup_paths()

        # 2. Now self.data is guaranteed to exist
        return [item["name"] for item in self.data.get(category, [])]

    def save_data(self):
        self._setup_paths()

        # Always save to the WRITABLE user_data_dir
        with open(self.save_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    # ------------------------
    # GETTERS
    # ------------------------

    def get_category(self, category):
        self._setup_paths()

        return self.data.get(category, [])

    def get_item(self, category, item_name):
        self._setup_paths()

        for item in self.data.get(category, []):

            if item["name"] == item_name:
                return item

        return None

    def get_item_names(self, category):
        self._setup_paths()

        return [item["name"] for item in self.data.get(category, [])]

    def get_categories(self):
        return list(self.data.keys())

    # ------------------------
    # ADD ITEM
    # ------------------------

    def add_item(self, category, name, image, description):
        self._setup_paths()

        if category not in self.data:
            return

        if self.get_item(category, name):
            return

        item = {
            "name": name,
            "image": image,
            "description": description,
        }

        self.data[category].append(item)

        self.save_data()

    # ------------------------
    # REMOVE ITEM
    # ------------------------

    def remove_item(self, category, name):
        self._setup_paths()

        if category not in self.data:
            return

        self.data[category] = [
            item for item in self.data[category] if item["name"] != name
        ]

        self.save_data()

    # ------------------------
    # UPDATE ITEM
    # ------------------------

    def update_item(self, category, name, new_data):
        self._setup_paths()

        for item in self.data.get(category, []):

            if item["name"] == name:

                item.update(new_data)

                self.save_data()

                return


# Singleton instance
inventory_manager = InventoryManager()
