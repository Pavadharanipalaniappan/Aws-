class Inventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, item_name, stock, price):
        if item_id in self.inventory:
            print(item_id, "already exists.")
        else:
            self.inventory[item_id] = {
                "item_name": item_name,
                "stock": stock,
                "price": price
            }
            print(item_id, "added to the inventory.")
    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item_details = self.inventory[item_id]
            print("Item ID:", item_id)
            print("Item Name:", item_details['item_name'])
            print("Stock:", item_details['stock'])
            print("Price: $%.2f" % item_details['price'])
        else:
            print(item_id, "does not exist.")

    def display_inventory(self):
        print("Inventory:")
        for item_id, item_details in self.inventory.items():
            print("Item ID:", item_id)
            print("Item Name:", item_details['item_name'])
            print("Stock:", item_details['stock'])
            print("Price: $%.2f" % item_details['price'])
inventory_manager = Inventory()
while True:
    print("\nMenu:")
    print("1. Add Item")
    print("2. Check Item Details")
    print("3. Display Inventory")
    print("4. Quit")
    choice = input("Enter your choice 1 or 2 or 3 or 4 : ")

    if choice == "1":
        item_id = input("Enter Item ID: ")
        item_name = input("Enter Item Name: ")
        stock = int(input("Enter Stock Quantity: "))
        price = float(input("Enter Item Price: $"))
        inventory_manager.add_item(item_id, item_name, stock, price)
    elif choice == "2":
        item_id = input("Enter Item ID to check details: ")
        inventory_manager.check_item_details(item_id)
    elif choice == "3":
        inventory_manager.display_inventory()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")