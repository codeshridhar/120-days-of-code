"""
Assignment 5: The Age Validator 🛡️
Take a user's age as input. Use conditionals to print:

If age < 0 or age > 150 → "Invalid age!"
If age < 13 → "Child"
If age 13-17 → "Teenager"
If age 18-59 → "Adult"
If age >= 60 → "Senior Citizen"
Hint: You'll need to check the invalid case FIRST.

Goal: Prove you understand condition ORDER and edge cases
"""

age = int(input("Enter your age : "))
if age < 0 or age > 150 : 
    result = "this is invalid age "
elif age < 13 :
    result = "Child"
elif age >= 13 and age <= 17 :
    result = "Teenager"
elif age >= 18 and age <= 59 :
    result = "Adult"
else :
    result = "SEnior Citizen"

print(result)