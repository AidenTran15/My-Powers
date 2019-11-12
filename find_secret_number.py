import random

secret_number = random.randint(0,10)
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won. ")
        break
else:
    print("Try it again")
