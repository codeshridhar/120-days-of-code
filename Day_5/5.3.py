# With match-case (new way — cleaner!)
#command = "start"
while True :
    command = input("enter the command ! ")
    match command:
        case "start"|"begin":
            print("Starting the system...")
        case "stop":
            print("Stopping the system...")
        case "restart":
            print("Restarting...")
        case _:
            print("Unknown command")
            break



day = input("enter the day : ")
while True:
    match day:
        case "monday"|"tuesday"|"wednesday"|"friday":
            print("no college")
        case "thursday":
            print("college if u want")
            break
        case "sunday"|"saturday":
            print("weekend")
        case _ :
            print("write proper spelling in lowercse")
            #pass