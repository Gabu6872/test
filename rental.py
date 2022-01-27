# program to manage the rental income flow for AllyBaba Rental property
def rental():

    monthly_rent = int(1000)
    late_fees = 0
    sign = str("$")
    
    month = input("Enter the month: ")  # prompt for entering the month
    day = int(input("Enter the day of the month: "))    # prompt for entering the day of the month
    trash_charges = int(input("Enter the amount of trash: "))   # prompt for entering trash charges
    water_charges = int(input("Enter the amount of water: "))   # prompt for entering  charges
    
    if day <= 3:    # if day of the month is <= to the due date for payment, no late fees is charged
        late_fees = 0
    

    elif day > 3 and day < 30:   # if day of the month is > to the due date for payment and < 30 days,
        late_fees = (day - 3)*5  # late fees is calculated as (day - 3)*5
   
    else:
        late_fees = 700 # if day does not satisfy the above conditions, late_fees is 700
    
    print(f"\n--- Rental Transaction for the month of {month} ------")
    print("Day the rent is paid\t\t", day)
    print("Monthly rent\t\t\t"+ sign + str(monthly_rent))
    print("Trash charges\t\t\t"+ sign + str(trash_charges))
    print("Water charges\t\t\t"+ sign + str(water_charges))
    print("Late fees charged\t\t"+ sign + str(late_fees))
   
    total = monthly_rent + trash_charges + water_charges + late_fees

    print(f"\nTotal due for {month}\t{sign}{total}")   # outputs the total amount to be paid

rental()
