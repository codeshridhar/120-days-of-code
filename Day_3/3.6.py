"""

Assignment 6: Daily Discipline Tracker 📋 (Your Day 3 Main Assignment)
Build exactly this:

Ask the user how many tasks they planned for today (integer).
Use a for loop to ask for the name of each task and whether it was completed (yes/no).
Count how many were completed.
Calculate the completion percentage.
Use if/elif/else to print a verdict:
100% → "Perfect execution. No excuses used."
70–99% → "Solid day. Protect this standard."
40–69% → "Average. You left energy on the table."
Below 40% → "Unacceptable. Tomorrow you repay this."

Then add a while loop section:
Keep asking "Do you want to add a leftover task that you finished? (yes/no)" until the user types no.
Each time they say yes, add +1 to the completed count AND +1 to total tasks, then update the percentage.
At the very end, print the final completed count and final percentage.
Goal: for + while + accumulation + conditionals — everything combined.

"""

numtask = int(input("Enter how many number of task u want to add in ur Daily Discipline Tracker 📋 ? "))

while numtask < 0 or numtask == 0:
    print("invalid number enter valid number ! ")
    numtask = int(input("Enter how many number of task u want to add in ur Daily Discipline Tracker 📋 ? "))

# for i in range (1 , numtask) : 
#     print(f"enter task {i}")
#     result = f"task {i}"
#     ip = numtask = int(input(f"Enter task {result} "))
#     print(ip)
    #print(result)

completed = 0
incompleted = 0
for i in range(1,numtask+1):
    task = input(f"enter task {i} : ")
    check = input(f"is task {i} completed ? yes/no ")
    if check.lower() == "yes" :
        completed += 1
        #break
    else:
        incompleted += 1

print(f"You completed {completed} out of {numtask} and {incompleted} tasks are still pending !")
average =((completed / numtask) * 100)
print(average)

# if average == 100:
#     print("Perfect execution. No excuses used")
# elif average >= 70 and average <= 99:
#     print("Solid day. Protect this standard.")
# elif average >= 40 and average <= 69:
#     print("Solid day. Protect this standard.")   
# elif average > 0 and average < 40:
#     print("Unacceptable. Tomorrow you repay this.")
# else:
#     print("do something ")
"""
my solution was ignoring the value after decimal point . e.g if 69.5 come there is no condition for that 

"""

if average >= 100:
    print("Verdict: Perfect execution. No excuses used.")
elif average >= 70:
    print("Verdict: Solid day. Protect this standard.")
elif average >= 40:
    print("Verdict: Average. You left energy on the table.")
else:
    print("Verdict: Unacceptable. Tomorrow you repay this.")



if average < 100 :
    ask = input("do u want to complete remaining tasks ? yes/no ")
    if ask.lower() == "yes":
        result = True
    else :
        print(f"{incompleted} are incomplete try ur best tomorrow")
        result = False
elif average == 100:
    result = False


while result:
    for i in range(1,incompleted+1):
        newcheck = input(f"is task {i} completed ? yes/no ")
        if newcheck.lower() == "yes" :
            completed += 1
            numtask += 1
            incompleted -= 1
        
        #break
        #else:
        #    completed -= 1
        #   incompleted += 1

    print(f"You again {completed} out of {numtask} and {incompleted} tasks are still pending !")
    average =((completed / numtask) * 100)
    print(average)  

    print(f"this is your final average {average}")
    print("all the best for tomorrow !")
    result = False





