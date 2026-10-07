"""
Diamond pattern
"""
rows = 10

for i in range(1,rows+1) : 
    for j in range(rows-i):
        print(" " , end="")
    for k in range (2*i-1) :
        print("*" , end="")
    print("")

for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" " , end="")
    for k in range(2*i-1):
        print("*",end="")
    print("")


print(" ")

rows = 10
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*",end = "")
    print("")
for i in range(1,rows):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*",end = "")
    print("")

rows = 20
for i in range(1,rows):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*" , end="")
    print("")





