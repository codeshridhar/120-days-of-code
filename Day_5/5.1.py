"""
pattern printing
right angle triangle 
"""

row = 10
for i in range (row):
    for j in range (row):
        print("*" * j)
    print("")

for i in range (row):
    for j in range(i):
        print("x", end="")
    print("")