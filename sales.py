from collections import defaultdict

dish_sales = defaultdict(int)

def track_dish_sales(dishes):
    for dish in dishes:
        dish_sales[dish] += 1

def generate_sales_report():
    print("\nSales Report:")
    for dish, count in sorted(dish_sales.items(), key=lambda item: item[1], reverse=True):
        print(f"{dish}: {count} orders")
