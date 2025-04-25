def calculate_fine(return_days, condition):
    fine = 0
    
    if return_days > 0:
        fine += return_days * 2  # Rs.2 per day late

    if condition == "damaged":
        fine += 50
    elif condition == "lost":
        fine += 500

    return fine


# Main program
days_late = int(input("Enter number of days after due date: "))
book_condition = input("Enter book condition (good/damaged/lost): ").lower()

total_fine = calculate_fine(days_late, book_condition)

print("\nTotal fine to be paid: ₹", total_fine)
