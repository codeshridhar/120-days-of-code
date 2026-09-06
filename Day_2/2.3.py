"""Assignment 2: The Broken Calculator 🔧
Write a program that takes two numbers from the user using input(). Without typecasting, try to add them and print the result. Then fix the code using int() or float() so it does REAL math. Print all 5 operations: +, -, *, /, %.

Goal: Prove you understand WHY input() needs typecasting and how all arithmetic operators work.

"""

numa = int(input("enter ur first number : "))
numb = int(input("enter secomd numb : "))
print("=" * 20)
print("for addition choose : + , add , addition or 1")
print("for substraction choose : - , sub , subtraction or 2")
print("for multiplication choose : * , mul , multiplication or 3")
print("for diviasion choose : / , div , division or 4 ")
print("for modulas choose : % , mod , modulas or 5")
operation = input("enter the operation u wanna perfrm on this operators ")
#operation1 = operation.lower()
print(operation)

if operation == "+" or operation.lower() == "add" or operation.lower() == "addition" or operation == "1" :
    result = numa + numb
elif operation == "-" or operation.lower() == "sub" or operation.lower() == "substraction" or operation == "2" :
    result = numa - numb
elif operation == "*" or operation.lower() == "mul" or operation.lower() == "multiplication" or operation == "3" :
    result = numa * numb
elif operation == "/" or operation.lower() == "div" or operation.lower() == "division" or operation == "4" :
    result = numa / numb
elif operation == "%" or operation.lower() == "mod" or operation.lower() == "modulasaction" or operation == "5" :
    result = numa % numb
else :
    result = " wait there is something  wrong !"
    print(f"something is wrong ! check your operation = {operation}  this dosent suppor ! ")
    print("=" * 30)
    print("Try : ")
    print("for addition choose : + , add , addition or 1")
    print("for substraction choose : - , sub , subtraction or 2")
    print("for multiplication choose : * , mul , multiplication or 3")
    print("for diviasion choose : / , div , division or 4 ")
    print("for modulas choose : % , mod , modulas or 5")

print(f"your answer is {numa} {operation} {numb} = {result}")