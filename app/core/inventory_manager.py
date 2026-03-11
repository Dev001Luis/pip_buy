import json
from pathlib import Path

DATA_FILE = Path("app/data/dev_inventory.json")


class InventoryManager:

    def __init__(self):
        self.data = {"languages": [], "frameworks": [], "softwares": []}
        self.load_data()

    def load_data(self):
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.save_data()

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    # Getters
    def get_category(self, category):
        return self.data.get(category, [])

    # Add item
    def add_item(self, category, item):
        if category in self.data:
            if item not in self.data[category]:
                self.data[category].append(item)
                self.save_data()

    # Remove item
    def remove_item(self, category, item):
        if category in self.data:
            if item in self.data[category]:
                self.data[category].remove(item)
                self.save_data()

    # Update item (replace old with new)
    def update_item(self, category, old_item, new_item):
        if category in self.data:
            if old_item in self.data[category]:
                idx = self.data[category].index(old_item)
                self.data[category][idx] = new_item
                self.save_data()


# Create a singleton instance
inventory_manager = InventoryManager()
