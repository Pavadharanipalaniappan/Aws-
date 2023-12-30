class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name, qty, price):
        item = (item_name, qty, price)
        self.items.append(item)
    
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item[0] != item_name]
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]*item[2]
        return total

cart = ShoppingCart()
while True:
    print("Please select an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Calculate total")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item_name = input("Enter item name: ")
        qty = float(input("Enter quantity: "))
        price = float(input("Enter price: "))
        cart.add_item(item_name, qty, price)
        print("Item added to cart.")
    elif choice == 2:
        item_name = input("Enter item name: ")
        cart.remove_item(item_name)
        print("Item removed from cart.")
    elif choice == 3:
        print("Current items in cart:")
        for item in cart.items:
            print(item[0], "-", item[1], "-", item[2])
    elif choice == 4:
        total = cart.calculate_total()
        print("Total price:", total)
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")