class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.table_reservations = []
        self.customer_orders = []
    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price
    def book_table(self, table_number):
        self.table_reservations.append(table_number)
    def take_customer_order(self, table_number, order):
        self.customer_orders.append((table_number, order))
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(item + ": $" + str(price))
    def print_table_reservations(self):
        print("Table Reservations:")
        for table in self.table_reservations:
            print("Table " + str(table) + " is reserved.")
    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.customer_orders:
            print("Table " + str(table) + " ordered: " + order)
restaurant = Restaurant()
while True:
    print("\nMenu:")
    print("1. Add Item to Menu")
    print("2. Book Table")
    print("3. Take Customer Order")
    print("4. Print Menu")
    print("5. Print Table Reservations")
    print("6. Print Customer Orders")
    print("7. Quit")
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    if choice == "1":
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: $"))
        restaurant.add_item_to_menu(item_name, item_price)
    elif choice == "2":
        table_number = int(input("Enter table number to book: "))
        restaurant.book_table(table_number)
    elif choice == "3":
        table_number = int(input("Enter table number: "))
        order = input("Enter customer's order: ")
        restaurant.take_customer_order(table_number, order)
    elif choice == "4":
        restaurant.print_menu()
    elif choice == "5":
        restaurant.print_table_reservations()
    elif choice == "6":
        restaurant.print_customer_orders()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7).")
