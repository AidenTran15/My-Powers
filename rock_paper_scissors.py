import random

humans = input("> ")
human = humans.lower()
comp_list = ["rock", "paper", "scissors"]
comp = random.choice(comp_list)

if human ==  "paper" and comp == "rock":
    print ("human win.")
elif human == "rock" and comp == "scissors":
    print("human win.")
elif human == "scissors" and comp == "paper":
    print ("human win.")
elif human == "paper" and comp == "scissors":
    print("comp wim.")
elif human == "rock" and comp == "paper":
    print("comp win.")
elif human == "scissors" and comp == "rock":
    print ("comp win.")
elif human == "rock" and comp == "rock":
    print("Tie.")
elif human == "paper" and comp == "paper":
    print ("Tie.")
elif human == "scissors" and comp == "scissors":
    print ('Tie. ')
