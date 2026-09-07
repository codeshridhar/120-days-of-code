"""
DAY 3 — LOOPS (for & while)
we use 
for() - when we know exact after how many steps to stop.
while() - we we dont know the steps but we know the condition of when to stop.


1) for()
"""
# 1 - for()
#for variable_name in range(...):
    # this block repeats
"""
here we know the steps so we know the range() here 
types of range :
a. range (stop) 
b. range (start , stop)
c. range (start , stop , jump)

range(5)        → 0, 1, 2, 3, 4       (starts at 0, stops BEFORE 5)
range(1, 6)     → 1, 2, 3, 4, 5       (starts at 1, stops BEFORE 6)
range(2, 10, 2) → 2, 4, 6, 8          (starts at 2, stops BEFORE 10, jumps by 2)
range(10, 0, -1)→ 10, 9, 8, ... 1     (countdown! jumps by -1)
"""
name = "Python"
for i in name:
    print(i)


# 2 - while()
"""
here we dont know exactly when to stop 
like : keep looping until user enter the perfect input 
"""
#while condition:
    # repeat this as long as condition is True
"""
Print numbers 1-100	== for ==	You know exactly how many times
Keep asking until valid input ==	while ==	You don't know how many tries
Process each item in a list	== for ==	Fixed number of items
Game loop (run until player quits) ==	while ==	Unknown duration
"""


#break
"""break the whole loop imidiately as soon as we hit the break condition

count = 10
while count > 0:
    print("hi)
    count -=1
    peint("count")
    if count == 5:
        break
    
        
this will break the loop when user hit the count 


"""
#continue
"""
this will just skip the current cycle and continue with the next one like in above example if we replace the break with the continue 
it will just skip the fifth one and continue with the 6th 
"""