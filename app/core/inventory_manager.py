import json
from pathlib import Path

DATA_FILE = Path("app/data/dev_inventory.json")


class InventoryManager:

    def __init__(self):

        self.data = {
            "items": [],
            "languages": [],
            "frameworks": [],
            "softwares": [],
        }

        self.load_data()

    # ------------------------
    # FILE MANAGEMENT
    # ------------------------

    def load_data(self):

        if DATA_FILE.exists():

            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)

        else:
            self.save_data()

    def save_data(self):

        with open(DATA_FILE, "w", encoding="utf-8") as f:
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
