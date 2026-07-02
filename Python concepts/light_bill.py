previous_reading = int(input("Enter Previous Meter Reading: "))
current_reading = int(input("Enter Current Meter Reading: "))

unit = current_reading - previous_reading

if unit < 0:
    print("Invalid meter readings!")
else:
    # Calculate energy charges
    if unit <= 100:
        charge = unit * 3
    elif unit <= 200:
        charge = (100 * 3) + ((unit - 100) * 5)
    else:
        charge = (100 * 3) + (100 * 5) + ((unit - 200) * 7)

    fix_charges = 80

    tax = charge * 0.05

    # Total bill
    total_bill = charge + fix_charges + tax

    # Display bill
    print("\n------ Electricity Bill ------")
    print("Previous Reading :", previous_reading)
    print("Current Reading  :", current_reading)
    print("unit Consumed   :", unit)
    print("Energy Charge    : ₹", charge)
    print("Fixed Charge     : ₹", fix_charges)
    print("Tax (5%)         : ₹", round(tax, 2))
    print("------------------------------")
    print("Total Bill       : ₹", round(total_bill, 2))