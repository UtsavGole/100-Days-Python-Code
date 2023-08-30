#tip calculator
print("Welcome to the tip calculator.")
total_bill=float(input("what was the total bill? "))
people_no=int(input("How many people to split the bill? "))
per=int(input("What percentage tip would you like  to give? 10,  12 or 15? "))
tip_amount=(per/100)*total_bill
total_amount=total_bill+tip_amount
amount_perhead=total_amount/people_no
print(f"Each person should  pay: ${amount_perhead}")