import json
import os
from kivy.app import App
from pathlib import Path


import os
from kivy.app import App
from kivy.utils import platform


class InventoryManager:
    def __init__(self):
        # 1. Get the app root regardless of OS
        if App.get_running_app():
            base_path = App.get_running_app().directory
        else:
            # Fallback for running script directly without App instance
            base_path = os.path.dirname(os.path.abspath(__file__))

        # 2. Define the Read-Only Data (Package Data)
        # This works on Windows (.\app\data) and Android (/data/user/0/...)
        self.default_data_file = os.path.join(
            base_path, "app", "data", "dev_inventory.json"
        )

        # 3. Define the Writable Data (Saves)
        if platform == "android":
            self.save_file = os.path.join(
                App.get_running_app().user_data_dir, "inventory_save.json"
            )
        else:
            # On PC, save in the same folder as the script for easy debugging
            self.save_file = os.path.join(
                base_path, "app", "data", "inventory_save.json"
            )

    def load_data(self):
        # Try to load from the "Save File" first (where changes live)
        if os.path.exists(self.save_file):
            with open(self.save_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        # Otherwise, load the default JSON packaged with the app
        elif os.path.exists(self.default_data_file):
            with open(self.default_data_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.save_data()

    def save_data(self):
        # Always save to the WRITABLE user_data_dir
        with open(self.save_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    # ------------------------
    # GETTERS
    # ------------------------

    def get_category(self, category):

        return self.data.get(category, [])

    def get_item(self, category, item_name):

        for item in self.data.get(category, []):

            if item["name"] == item_name:
                return item

        return None

    def get_item_names(self, category):

        return [item["name"] for item in self.data.get(category, [])]

    def get_categories(self):
        return list(self.data.keys())

    # ------------------------
    # ADD ITEM
    # ------------------------

    def add_item(self, category, name, image, description):

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

        for item in self.data.get(category, []):

            if item["name"] == name:

                item.update(new_data)

                self.save_data()

                return


# Singleton instance
inventory_manager = InventoryManager()
