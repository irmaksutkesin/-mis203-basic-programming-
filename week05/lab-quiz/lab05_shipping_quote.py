def calculate_subtotal(unit_price, quantity):
    return unit_price * quantity

def calculate_discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10
    return 0.0

def calculate_shipping_fee(subtotal):
    if subtotal >= 150:
        return 0.0
    return 20.0

def calculate_final_total(subtotal, discount_rate, shipping_fee):
    return (subtotal * (1 - discount_rate)) + shipping_fee

assert calculate_subtotal(10, 5) == 50
assert calculate_discount_rate(100) == 0.10
assert calculate_shipping_fee(150) == 0.0

def process_order(order_name, quantity):
    unit_price = 10
    subtotal = calculate_subtotal(unit_price, quantity)
    discount_rate = calculate_discount_rate(subtotal)
    shipping = calculate_shipping_fee(subtotal)
    final_total = calculate_final_total(subtotal, discount_rate, shipping)
    print(order_name, "Total:", final_total)

process_order("Order 1", 5)
process_order("Order 2", 20)
