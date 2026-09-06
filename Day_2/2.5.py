"""
Build a "Student Performance Evaluator" script that does the following:

Asks the user for their name.
Asks the user for marks in 3 subjects (out of 100 each). Make sure to convert the input to numbers (float or int).
Calculates the Total Marks (out of 300) and Average Percentage.
Uses if / elif / else logic to evaluate the result:
Average >= 90: Grade A+ (Print: "Outstanding performance!")
Average >= 75: Grade A (Print: "Great job!")
Average >= 60: Grade B (Print: "Good, but room to grow.")
Average >= 40: Grade C (Print: "Warning: Low score.")
Below 40: FAIL (Print: "Failed. Immediate action required.")
Checks if any individual subject mark is below 35. If yes, print a specific warning: "Failed due to backlog in an individual subject." regardless of the average.
"""
name = input("Enter your Name : ")
print("Now enter 3 subject marks :")
suba = float(input("Marks of subject A out of 100 . "))
subb = float(input("Marks of subject B out of 100 . "))
subc = float(input("Marks of subject C out of 100 . "))
total = suba+subb+subc
totalpercentage = (total/300)*100
print(f"{name} you got total marks {total} in all 3 subjects which makes your percentage {totalpercentage:.2f}")
if suba < 35 or subb < 35 or subc < 35:
    grade = "-"
    remark = "Failed due to backlog in an individual subject."
elif totalpercentage >= 90:
    grade = "A+"
    remark = "Outstanding performance!"
elif totalpercentage >= 75 :
    grade = "A"
    remark = "Great job!"
elif totalpercentage >= 60 :
    grade = "B"
    remark =  "Good, but room to grow."
elif totalpercentage >= 40 :
    grade = "C"
    remark = "Warning: Low score."
elif totalpercentage < 40 :
    grade = "F"
    remark = " You re failed !"
else :
    print()

print(f"{name} you got grade {grade} over so thats {remark}")
