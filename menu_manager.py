
menu = {}

def add_dish(dish_name, price):
    menu[dish_name] = price
    print(f"Dish '{dish_name}' added to the menu.")

def modify_dish(dish_name, new_price):
    if dish_name in menu:
        menu[dish_name] = new_price
        print(f"Dish '{dish_name}' price updated to {new_price}.")
    else:
        print(f"Dish '{dish_name}' not found.")

def remove_dish(dish_name):
    if dish_name in menu:
        del menu[dish_name]
        print(f"Dish '{dish_name}' removed from the menu.")
    else:
        print(f"Dish '{dish_name}' not found.")

def display_menu():
    print("\nMenu:")
    for dish, price in menu.items():
        print(f"{dish}: ${price}")
