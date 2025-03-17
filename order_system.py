def get_menu_dictionary():
    """
    Returns a dictionary containing menu items with categories, names, and prices.
    """
    return {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 4.99,
            "Vegetarian": 4.29
        },
        "Taco": {
            "Chicken": 2.49,
            "Beef": 2.79,
            "Vegetarian": 2.19
        },
        "Drink": {
            "Soda": 1.99,
            "Water": 1.49,
            "Juice": 2.29
        }
    }

def get_menu_items_dict(menu):
    """
    Returns a dictionary mapping menu item numbers to their details.
    """
    menu_items = {}
    i = 1
    for category, items in menu.items():
        for name, price in items.items():
            menu_items[i] = {"Category": category, "Item name": f"{category} - {name}", "Price": price}
            i += 1
    return menu_items

def print_menu_heading():
    """
    Prints the heading for the menu.
    """
    print("\n--- MENU ---")
    print(f"{'No.':<5}{'Category':<15}{'Item':<20}{'Price'}")
    print("-" * 50)

def print_menu_line(index, category, item, price):
    """
    Prints a formatted menu line.
    """
    print(f"{index:<5}{category:<15}{item:<20}${price:.2f}")

def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.
    """
    order = []
    menu_items = get_menu_items_dict(menu)

    print("\nWelcome to the Generic Take Out Restaurant!")

    while True:
        # Mostrar el menú
        print_menu_heading()
        for i, item in menu_items.items():
            print_menu_line(i, item["Category"], item["Item name"], item["Price"])

        # Solicitar selección del usuario
        menu_selection = input("\nEnter the menu item number you want to order: ")

        # Actualizar el pedido
        order = update_order(order, menu_selection, menu_items)

        # Preguntar si desea ordenar más
        another_order = input("\nWould you like to order anything else? (Press 'n' or 'N' to finish): ")
        if another_order.lower() == 'n':
            print("\nThank you for your order!\n")

            # Calcular el total del pedido
            order_total = sum(item["Price"] * item["Quantity"] for item in order)

            break

    return order, round(order_total, 2)

def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.
    """
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        if menu_selection in menu_items:
            item_name = menu_items[menu_selection]["Item name"]
            price = menu_items[menu_selection]["Price"]

            quantity = input(f"How many of {item_name} would you like? ")
            quantity = int(quantity) if quantity.isdigit() else 1

            order.append({"Item name": item_name, "Price": price, "Quantity": quantity})
            print(f"\nAdded {quantity}x {item_name} to your order.")
        else:
            print(f"\n'{menu_selection}' is not a valid menu item number. Please select a valid number.")
    else:
        print("\nInvalid input. Please enter a valid number.")

    return order

def print_receipt_heading():
    """
    Prints the heading for the receipt.
    """
    print("\n--- RECEIPT ---")
    print(f"{'Item':<30}{'Qty':<5}{'Price'}")
    print("-" * 50)

def print_receipt_line(item_name, price, quantity):
    """
    Prints a formatted receipt line.
    """
    print(f"{item_name:<30}{quantity:<5}${price * quantity:.2f}")

def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.
    """
    for item in receipt:
        print_receipt_line(item["Item name"], item["Price"], item["Quantity"])

def print_receipt_footer(total_price):
    """
    Prints the footer with the total price of the receipt.
    """
    print("-" * 50)
    print(f"{'TOTAL':<35}${total_price:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    meals = get_menu_dictionary()
    receipt, total_price = place_order(meals)

    print("\nThis is what we are preparing for you.\n")
    print_receipt_heading()
    print_itemized_receipt(receipt)
    print_receipt_footer(total_price)