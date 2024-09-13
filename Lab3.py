user_input_income = float(input("Enter amount of income you earned in 2023: "))
user_input_relationship = input("Are you married or single (m/s)?: ")

if user_input_relationship == "m": 
    if user_input_income <= 22000:
        tax1 = user_input_income * 0.1
        print(f"Tax amount for married: {tax1:.2f}")
    elif user_input_income <= 89450:
        tax2 = user_input_income * 0.12
        print(f"Tax amount for married: {tax2:.2f}")
    elif user_input_income <= 190750:
        tax3 = user_input_income * 0.22
        print(f"Tax amount for married: {tax3:.2f}")
    elif user_input_income > 190750:
        print("Income is above the taxable threshold for married status.")
    
elif user_input_relationship == "s": 
    if user_input_income <= 11000:
        tax4 = user_input_income * 0.1
        print(f"Tax amount for single: {tax4:.2f}")
    elif user_input_income <= 44725:
        tax5 = user_input_income * 0.12
        print(f"Tax amount for single: {tax5:.2f}")
    elif user_input_income <= 95375:
        tax6 = user_input_income * 0.22
        print(f"Tax amount for single: {tax6:.2f}")
    elif user_input_income > 190750:
        print("Income is above the taxable threshold for single status.")
