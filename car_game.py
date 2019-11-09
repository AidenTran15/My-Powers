class CarGame:
    def __init__(self):
        self.command = ""
        self.started = False
    
    def start(self):
        while True:
            self.command = input("> ").lower()
            if self.command == "start":
                if self.started: 
                    print("car is already started")
                else:
                    self.started = True
                    print("car started...ready to go")
                    
            elif self.command == "stop":
                if  not self.started:
                    print("car is already stopped")
                else:
                    self.started = False
                    print("car stopped")
            elif self.command =="help":
                print("""
                    start - to start the car
                    stop - to stop the car
                    quit - to quit""")
            elif self.command == "quit":
                break
        else:
            print("sorry, I don't understand ")