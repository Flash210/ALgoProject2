# main.py
from menu_manager import add_dish, modify_dish, remove_dish, display_menu
from order_manager import create_order, check_order_exists, calculate_total
from payment import update_payment_status, display_payment_status
from sales import track_dish_sales, generate_sales_report

add_dish("Kouskous", 5)
add_dish("Kaftaji", 8)
add_dish("Ma9rouna", 7)

display_menu()

create_order("Houcem", ["Kouskous", "Kaftaji"])
create_order("Ahmed", ["Ma9rouna", "Kouskous"])

print(check_order_exists("ahmed", ["Kaftaji", "Kaftaji"]))  # True

print(f"houcem's total: ${calculate_total(['Kaftaji', 'Kouskous'])}")

update_payment_status("houcem", True)

display_payment_status()

track_dish_sales(["Kouskous", "Ma9rouna", "Kaftaji"])

generate_sales_report()

modify_dish("Kaftaji", 9)
remove_dish("Ma9rouna")

display_menu()
