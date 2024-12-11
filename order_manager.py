
from menu_manager import menu

orders = set()

def create_order(customer_name, dishes):
    order = (customer_name, tuple(dishes))
    if order not in orders:
        orders.add(order)
        print(f"Order for {customer_name} added.")
    else:
        print(f"Order for {customer_name} already exists.")

def check_order_exists(customer_name, dishes):
    order = (customer_name, tuple(dishes))
    return order in orders

def calculate_total(dishes):
    total = 0
    for dish in dishes:
        if dish in menu:
            total += menu[dish]
        else:
            print(f"Dish '{dish}' not found in menu!")
    return total
