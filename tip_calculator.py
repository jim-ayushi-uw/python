# This is a Tip calculator. It takes the amount of bill, number of person and amount of tip and divide the bill accordingly.

print("Welcome to tip Calculator!")
bill = float(input("What was the amount of the bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill * tip/100 + bill
bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person, 2)
print(f"Each person shoud pay {final_amount}")
