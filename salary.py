def calculate_net_salary(category, monthly_salary=0, hourly_rate=0, present_days=0, absent_days=0, incentives=0, income_tax=0):
    if category.lower() == "permanent":
        # For permanent: salary - tax + incentives (assuming fixed monthly salary, not affected by present days)
        gross = monthly_salary + incentives
        net = gross - income_tax
    elif category.lower() == "temporary":
        # For temporary: paid only for present days, plus incentives, minus tax
        working_salary = present_days * hourly_rate * 8  # Assuming 8 hours/day
        gross = working_salary + incentives
        net = gross - income_tax
    else:
        return "Invalid employee category."

    return net


# Main program
print("Employee Salary Calculator\n")

emp_type = input("Enter employee type (permanent/temporary): ").strip().lower()

if emp_type == "permanent":
    salary = float(input("Enter monthly salary: ₹"))
    incentives = float(input("Enter incentives/bonus: ₹"))
    tax = float(input("Enter income tax: ₹"))
    net_salary = calculate_net_salary("permanent", monthly_salary=salary, incentives=incentives, income_tax=tax)
elif emp_type == "temporary":
    hourly = float(input("Enter hourly rate: ₹"))
    present = int(input("Enter number of present days: "))
    incentives = float(input("Enter incentives/bonus: ₹"))
    tax = float(input("Enter income tax: ₹"))
    net_salary = calculate_net_salary("temporary", hourly_rate=hourly, present_days=present, incentives=incentives, income_tax=tax)
else:
    print("Invalid employee type.")
    net_salary = None

if net_salary is not None:
    print(f"\nNet Salary for {emp_type.capitalize()} Employee: ₹{net_salary:.2f}")
