command = ""
started = False
while command == "quit":
    command = input("> ").lower()
    if command == "start":
        print("car started. Ready to go")
    elif command == "stop":
        print("car stop")
    elif command == "quit":
        print("good bye, see you later")
        break
    elif command == "help":
        print("""
        start: to start the car
        stop: to stop the car
        quit: to quit""")
    else:
        print("Sorry,I don't understand, type help to have a introdution")
    

