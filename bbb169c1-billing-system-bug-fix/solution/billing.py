def calculate_invoice_total(items, discount_percent):
    """Return the invoice total after applying a percentage discount."""
    subtotal = 0.0
    for item in items:
        subtotal += item["price"] * item["quantity"]
    discount = subtotal * discount_percent / 100
    return round(subtotal - discount, 2)


if __name__ == "__main__":
    invoice_items = [
        {"name": "Keyboard", "price": 50.00, "quantity": 2},
        {"name": "Mouse", "price": 25.00, "quantity": 1},
        {"name": "Monitor", "price": 200.00, "quantity": 1},
    ]
    print("Invoice total:", calculate_invoice_total(invoice_items, 10))
