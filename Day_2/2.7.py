"""
Assignment 6: The Ultimate Combo 🏆 (Boss Level)
Build a Mini ATM:

Ask the user for their PIN (assume correct PIN is 1234).
If PIN is wrong → print "Access Denied" and stop.
If PIN is correct → ask "Enter amount to withdraw".
Assume balance is 5000.
If amount > balance → print "Insufficient funds".
If amount <= 0 → print "Invalid amount".
Otherwise → print "Dispensing ₹___" and show remaining balance.
Goal: Combine typecasting + comparison + nested conditionals in a real-world scenario.


"""

pin = 1234
balance = 5000
userpin = int(input("enter 4 digit pin "))
if userpin == pin:
    amount = int(input("enter the ampunt u wanna withdrw ? "))
    if amount > balance :
        print("Insufficiant balance !")
    elif amount <= 0 :
        print("invalid value")
    else:
        print(f"Disspending rupees {amount} from {balance}")
        updatedbalance = balance - amount
        print(f"{updatedbalance} this is your remaining amount")
else:
    print("In correct pin try again") 

