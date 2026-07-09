print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? ru"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ru{final_amount}")
print(f"Each person should pay: ru{round(final_amount)}")



'''street_name = "Abbey Road"
print(street_name[4] + street_name[7])

print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(type(a))'''