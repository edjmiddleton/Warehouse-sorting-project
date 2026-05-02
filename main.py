class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item_name, quantity, batch_id):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if item_name not in self.stock:
            self.stock[item_name] = []

        self.stock[item_name].append({
            "batch": batch_id,
            "quantity": quantity
        })

        print(f"Added batch {batch_id}: {quantity} {item_name}")

    def remove_stock(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if item_name not in self.stock or not self.stock[item_name]:
            print("Item not found.")
            return

        total_available = sum(batch["quantity"] for batch in self.stock[item_name])

        if total_available < quantity:
            print("Not enough stock available.")
            return

        amount_to_remove = quantity

        while amount_to_remove > 0:
            oldest_batch = self.stock[item_name][0]

            if oldest_batch["quantity"] <= amount_to_remove:
                amount_to_remove -= oldest_batch["quantity"]
                print(f"Removed full batch {oldest_batch['batch']}")
                self.stock[item_name].pop(0)
            else:
                print(f"Removed {amount_to_remove} from batch {oldest_batch['batch']}")
                oldest_batch["quantity"] -= amount_to_remove
                amount_to_remove = 0

        if not self.stock[item_name]:
            del self.stock[item_name]

    def show_stock(self):
        print("\nCurrent warehouse stock:")

        if not self.stock:
            print("Warehouse is empty.")
            return

        total_items = 0

        for item_name, batches in self.stock.items():
            print(f"\n{item_name}:")

            for batch in batches:
                print(f"  Batch {batch['batch']}: {batch['quantity']}")
                total_items += batch["quantity"]

        print(f"\nTotal items in warehouse: {total_items}")


def main():
    warehouse = Warehouse()

    while True:
        print("\nWarehouse Management System - Tier 2")
        print("1. Add batch")
        print("2. Remove stock")
        print("3. Show stock")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item_name = input("Item name: ")
            quantity = int(input("Quantity to add: "))
            batch_id = input("Batch ID: ")
            warehouse.add_stock(item_name, quantity, batch_id)

        elif choice == "2":
            item_name = input("Item name: ")
            quantity = int(input("Quantity to remove: "))
            warehouse.remove_stock(item_name, quantity)

        elif choice == "3":
            warehouse.show_stock()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")


main()