class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if item_name in self.stock:
            self.stock[item_name] += quantity
        else:
            self.stock[item_name] = quantity

        print(f"Added {quantity} {item_name}.")

    def remove_stock(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if item_name not in self.stock:
            print("Item not found.")
            return

        if self.stock[item_name] < quantity:
            print("Not enough stock available.")
            return

        self.stock[item_name] -= quantity
        print(f"Removed {quantity} {item_name}.")

        if self.stock[item_name] == 0:
            del self.stock[item_name]

    def show_stock(self):
        print("\nCurrent warehouse stock:")

        if not self.stock:
            print("Warehouse is empty.")
        else:
            for item_name, quantity in self.stock.items():
                print(f"{item_name}: {quantity}")


def main():
    warehouse = Warehouse()

    while True:
        print("\nWarehouse Management System - Tier 1")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Show stock")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item_name = input("Item name: ")
            quantity = int(input("Quantity to add: "))
            warehouse.add_stock(item_name, quantity)

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