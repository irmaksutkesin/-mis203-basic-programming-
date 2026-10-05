def main():
    # Input collection
    order_amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_quantity = int(input("Enter requested quantity: "))
    is_member_input = input("Is the customer a member? (yes/no): ").strip().lower()

    is_member = is_member_input in ["yes", "y"]

    # 1. Validation and Stock Check (Rejection cases)
    if requested_quantity <= 0 or order_amount <= 0:
        print("\n[REJECTED] Invalid quantity or order amount.")
        return

    if requested_quantity > available_stock:
        print("\n[REJECTED] Insufficient stock.")
        return

    # 2. Approval and Discount Calculation
    discount = 0.0
    # Logical operator (and) usage
    if is_member and order_amount >= 500:
        discount = 0.10
        approval_reason = "Order approved with a 10% member discount."
    else:
        approval_reason = "Order approved at standard price."

    final_price = order_amount * (1 - discount)

    # 3. Output display (For approved orders only)
    print(f"\n[APPROVED] {approval_reason}")
    print(f"Final Price: {final_price:.2f} TRY")


if __name__ == "__main__":
    main()
