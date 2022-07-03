print("Welcome to he tip calculator!")
bill_amount = float(input("What was the total bill?"))
tip_percent = float(input("How much tip would you like to give?"))
final_tip_percent = bill_amount * (tip_percent / 100) + bill_amount

split_amt = float(input("How many people to split the bill?"))

each_person = final_tip_percent / split_amt 

print(round(each_person , 2))