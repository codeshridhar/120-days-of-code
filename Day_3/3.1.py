"""
Assignment 1: The Number Printer 🔢
Write a for loop that prints all numbers from 1 to 50 that are divisible by both 3 and 5. Use range() and if inside the loop.

Goal: Combine for + range() + % + if.
"""
j = 1
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0 :
        print(f"{j}. {i}")
        #j += 1
    i += 1