command = ""
started = False
while command != "quit":
    command = input("> ")
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car start. Ready to go")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started  = False
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
    

