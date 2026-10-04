# Summary tracking variables
tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    # 1. Customer Name / Exit Condition
    name = input("Customer name (or q to quit): ")
    if name.lower() == 'q':
        break

    # 2. Age Input & Validation
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    # 3. Day Input & Validation
    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    # 4. Student Input & Validation
    student_input = input("Student (yes/no): ").strip().lower()
    if student_input not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    is_student = (student_input == "yes")

    # 5. Base Price Calculation
    if day == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

    # 6. Apply Discount Rules (Strict Order)
    if age < 6:
        discount_rate = 1.00
        category = "Free"
    elif age >= 65:
        discount_rate = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount_rate = 0.40
        category = "Child"
    elif is_student and age <= 25:
        discount_rate = 0.30
        category = "Student"
    else:
        discount_rate = 0.00
        category = "Standard"

    # Calculate final price
    final_price = base_price * (1 - discount_rate)

    # Output formatted result
    print(f"{name}: {final_price:.2f} TRY ({category})")

    # Update summary tracking variables
    tickets_sold += 1
    total_revenue += final_price
    if final_price == 0:
        free_tickets += 1

# Final Summary Section
if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")

