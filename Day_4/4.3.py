"""
Create Day_4/day4.py.

Build an upgraded “Discipline List Manager”:

Start with an empty list planned_tasks = []
Ask how many tasks the user wants to plan. Use a for loop to collect task names and .append() each one into the list.
Print the full list of planned tasks with numbers (1-based index).
Create two more empty lists: completed = [] and pending = []
Loop through planned_tasks:
Ask yes/no for each.
If yes → append to completed
If no → append to pending
Print:
All completed tasks
All pending tasks
Completion percentage (use round(pct, 2))
Verdict (same scale as Day 3):
100% → “Perfect execution. No excuses used.”
70–99% → “Solid day. Protect this standard.”
40–69% → “Average. You left energy on the table.”
Below 40% → “Unacceptable. Tomorrow you repay this.”
Extra requirement (forces real list thinking):
Ask the user for a task name to search.
If it exists in completed, print "Already done."
Else if it exists in pending, print "Still pending. Do it now."
Else print "Task not found in today’s list."
Push Day_4/day4.py to GitHub.
"""
print("="  * 40)
print("x"  * 40)
index = 1
planned_tasks = []
completed = []
remaining = []
completed2 = []
# print("x"  * 40)
# print("="  * 40)
numtask = int(input("Enter how many task you want to add ? "))
for i in range(1,numtask+1):
    task = input(f"Enter task {i} : ")
    planned_tasks.append(task)
print(f"this are planned {numtask} tasks for today : ")
for taskk in planned_tasks:
    print(f"{index} . {taskk}")
    index += 1

print("X"  * 40)
print("="  * 40)

print("now its time for the first check in of the day to evaluate how many taks you have completed so far ! ")
for taks in planned_tasks:
    print("----" * 10)
    status = input(f"did you complete the ->{taks}<- task ? ? (answer in yes/no) ")
    while True:
        if status.lower() == "yes" or status.lower() == "no":
            print(f"responce for ->{taks}<- is added !")
            break
        else:
            print(f"{status} is invalid it should be only yes or no")
            status = input(f"did you complete the ->{taks}<- task ? ? (answer in yes/no) ")
    if status.lower() == "yes" :
        completed.append(taks)
    else :
        remaining.append(taks)
    print("----" * 10)
    #if status.lower == "yes":
        
print(f"congratulations you have completed the following tasks of the day =>{completed}")

avscore1 = round((len(completed)/len(planned_tasks))*100,2)
if avscore1 == 100 :
    print("Perfect execution. No excuses used.")
elif avscore1 > 70 :
    print("Solid day. Protect this standard.")
elif avscore1 > 40 :
    print("Average. You left energy on the table.")
else :
    print("Unacceptable. Tomorrow you repay this.")


print(f" This are the still remaining tasks {remaining}")
while True :
    stask = input("search for thee task you want to check ")
    if stask in remaining :
        print("TASK remaing do it now !")
    else :
        print("task not in remaing ")
    r = input("want to do it again ? >no for stoping< ")
    if r.lower() == "no":
            break
    

while True :
    print("ask")
    r = input("want to do it again ? >no for stoping< ")
    if r.lower() == "no":
        break


print("now its time for the last check in of the day to evaluate how many taks you have completed from remaining tasks ! ")
for task in remaining:
    #print(f"did you completed the -> {task} <-  answer yes/no")
    answer = input(f"did you completed the -> {task} <-  answer yes/no : ")
    while True:
        if answer.lower() == "yes" or answer.lower() == "no":
            break
        else:
            answer = input(f" ANSWER YES / NO . did you completed the -> {task} <-  answer yes/no : ")
    if answer.lower() == "yes" :
        completed.append(task)
        remaining.remove(task)



avscore1 = round((len(completed)/len(planned_tasks))*100,2)
match avscore1:
    case 100 :
        print("Perfect execution. No excuses used")
    case score if score > 70:
        print("Solid day. Protect this standard.")
    case score if score > 40:
        print("Average. You left energy on the table.")
    case _ :
        print("Unacceptable. Tomorrow you repay this.")
    

# if avscore1 == 100 :
#     print("Perfect execution. No excuses used.")
# elif avscore1 > 70 :
#     print("Solid day. Protect this standard.")
# elif avscore1 > 40 :
#     print("Average. You left energy on the table.")
# else :
#     print("Unacceptable. Tomorrow you repay this.")