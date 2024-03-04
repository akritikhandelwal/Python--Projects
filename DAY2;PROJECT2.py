#DAY 2: PROJECT 2; TIP CALCULATOR 
print("Welcome to the tip calculator. ")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
calc = (float(total_bill) + (int(tip)/100)*float(total_bill)) / int(people)
print("Each person should pay: $" + str(round(calc,2)))