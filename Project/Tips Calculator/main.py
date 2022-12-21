print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split_people = int(input("How many people to split the bill? "))


tips = percentage_tip / 100
paid_per_person = (total_bill * (1 + tips)) / split_people


print(f"Total bill is ${total_bill}\nTip {percentage_tip}%\nThere is(are) {split_people} person(s)\nEach person should pay: ${paid_per_person:.2f}")