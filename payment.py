
payment_status = {}

def update_payment_status(customer_name, status):
    payment_status[customer_name] = status
    status_text = "paid" if status else "not paid"
    print(f"Payment status for {customer_name} updated to {status_text}.")

def display_payment_status():
    print("\nPayment Status:")
    for customer, status in payment_status.items():
        status_text = "Paid" if status else "Not Paid"
        print(f"{customer}: {status_text}")
