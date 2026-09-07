"""
Assignment 3: The Password Gate 🔐
Use a while loop to keep asking the user for a password until they type "secret123". Count how many attempts they took. If they get it right, print "Access granted in X attempts". If they fail 5 times, print "Account locked" and break out.

Goal: while loop + counter + break.

"""

password = "secret123"
userpassword = input("ente the password ")
attempt = 4
while True :
    if userpassword == password:
        print("permission granted !")
        break

    print(f"wrong attempt try again {attempt} attempts left")
    userpassword = input("ente the password ")
    attempt -= 1
    if attempt == 0:
        print("u hit the limit or daily tries ! account is locked for today .")
        break


