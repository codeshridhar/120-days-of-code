"""
Assignment 3: Even or Odd Judge ⚖️
Take a number from the user. Use the % operator and an if-else statement to print whether the number is Even or Odd.

Goal: Prove you understand modulo + conditionals together.

"""

num = int(input("the number u want to check ! "))
if num % 2 == 0 :
    result = "number is even"
elif num % 2 != 0 :
    result = "number is odd"
else:
    result = "haha dont know about the number but something is ODD here . may be the number u entered !"
# i know this else has no job here because id the number is wrong data type it will throw the error at the % step !
print(f"{num} is {result}")