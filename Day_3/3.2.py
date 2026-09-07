"""
Assignment 2: The Sum Machine ➕
Ask the user how many numbers they want to add. Use a for loop to take that many inputs, accumulate the total, and print the sum AND average at the end.

Goal: Master the accumulation pattern with user input.
"""
sum = 0
num = int(input("enter how many numbers you want to add ? "))
while num < 0 :
    print("incalid try again :")
    num = int(input("enter how many numbers you want to add ? "))
for i in range(num+1):
    sum = sum + i
    #i += 1

average = sum/num

print(f"you asked for {num} sum their sum is {sum} and average is {average}")