"""Assignment 5: The Factorial Calculator 🧮
Ask the user for a positive integer n. Use a for loop to calculate n! (factorial). Example: 5! = 5 × 4 × 3 × 2 × 1 = 120. Use the accumulation pattern (but with multiplication instead of addition).

Hint: Initialize your accumulator to 1, not 0. Think about why.

Goal: Accumulation pattern with multiplication."""


numuser = int(input("enter the number to calculate the factorial : "))
while numuser < 0:
    print("invalid input number must be positive integer")
    print("try some positive number")
    numuser = int(input("enter the number to calculate the factorial : "))


a = 1
#for i in range (numuser,1):
#    print(i)
#    facto = facto * i
#    i -= 1
facto = numuser
for i in range (numuser-1 , 0 , -1):
    #print(i)
    print(f"step. {a} . {facto} * {i} = {facto * i}")
    facto = facto * i
print(f"factorial of {numuser} is {facto}")

