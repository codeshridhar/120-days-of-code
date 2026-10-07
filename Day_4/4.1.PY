"""- Ask user to enter 7 numbers (collect in a list)
- Print: max, min, sum, average
- Print all numbers above average
- Print all numbers below average
"""
list = []
print("hello user enter the 7 numbers : ")
for i in range (1,8):
    num = int(input(f"enter the number {i} : "))
    list.append(num)
print(list)
for item in list:
    print(item)


max = max(list)
min = min(list)
summ = sum(list)
avg = summ/len(list)
abovel = []
belowl = []
bl = 0
al = 0
print(f" this is minimun : {min} this is maximum : {max} this is sum : {summ} this is average :{avg:.2f}")
for i in  list : 
    if i > avg :
        abovel.append(i)
        al += 1
    else :
        belowl.append(i)
        bl += 1
print(f"{al} are total number above average ==> {abovel}")
print(f"{bl} are total number above average ==> {belowl}")