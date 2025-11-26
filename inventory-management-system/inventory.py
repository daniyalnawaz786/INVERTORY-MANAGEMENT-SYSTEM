import json
import os

class Inventory:
    def __init__(self, file_path="inventory.json"):
        self.file_path = file_path
        self.items = self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    data = file.read().strip()
                    if not data:
                        return []
                    return json.loads(data)
            except json.JSONDecodeError:
                return []
        return []

    def save_inventory(self):
        with open(self.file_path, "w") as file:
            json.dump(self.items, file, indent=4)

    def add_item(self, name, quantity, price):
        item_id = len(self.items) + 1
        item = {
            "id": item_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.items.append(item)
        self.save_inventory()
        print("Item added successfully!")

    def update_quantity(self, item_id, quantity):
        for item in self.items:
            if item["id"] == item_id:
                item["quantity"] = quantity
                self.save_inventory()
                print("Item quantity updated!")
                return
        print("Item not found!")

    def delete_item(self, item_id):
        original_len = len(self.items)
        self.items = [item for item in self.items if item["id"] != item_id]

        if len(self.items) < original_len:
            self.save_inventory()
            print("Item deleted successfully!")
        else:
            print("Item not found!")

    def view_items(self):
        if not self.items:
            print("Inventory is empty.")
            return

        print("\n--- Inventory List ---")
        for item in self.items:
            print(f"{item['id']}. {item['name']} | Qty: {item['quantity']} | Price: {item['price']}")

    def search_item(self, name):
        results = [item for item in self.items if name.lower() in item["name"].lower()]
        return results

    # NEW FUNCTION ✔
    def get_item_names(self):
        return [item["name"] for item in self.items]
