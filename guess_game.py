import random

class GuessingGame:
  
  def __init__(self):
    self.secret_number = random.randint(0,10)
    self.guess_limit = 100
    self.guess_count = 0
  
  def play(self):
    while self.guess_count < self.guess_limit:
      guess = int(input("guess: "))
      self.guess_count += 1
      if guess == self.secret_number:
        print("you won")
        break
      if guess < self.secret_number:
          print("this nummber is so small")
      if guess > self.secret_number:
          print("this number is so large")
