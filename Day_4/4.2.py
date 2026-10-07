"""
- Collect 10 names from user
- Find and print any duplicate names
- Print unique names only
- Hint: use .count()
"""
nameli = []
uniqueli = []
duplicateli = []
print("enter 10 names")
for i in range (1 , 11) :
    nam = input(f"enter the name {i} : ")
    nameli.append(nam)

for name in nameli : 
    if nameli.count(name) > 1 and name not in duplicateli :
        duplicateli.append(name)
    
    elif nameli.count(name) == 1:
        uniqueli.append(name)
    else :
        ("sonethig went wrong !")



print(f"this is the name that appears frequently ! {duplicateli}")
print(f"this is the name that appears once ! {uniqueli}")
