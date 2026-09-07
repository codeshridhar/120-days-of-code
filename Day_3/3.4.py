"""
Assignment 4: The Skipper ⏭️
Use a for loop with range(1, 21). Print all numbers EXCEPT multiples of 4. Use continue to skip them. At the end, print how many numbers were skipped using a counter.

Goal: continue + counter pattern.
"""
count = 0
nums = []
#collection of same objects that is string 
for i in range(1,21):
    if i % 4 == 0:
        count += 1
        nums.append(i)
        #append is to add in the string 
        continue
    i += 1

print(f"{count}")
print("numbers are as follow")
print(nums)