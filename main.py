import click
from myPowers.guess_game import GuessingGame
from myPowers.car_game import CarGame


guessGame = None
carGame = None



@click.group()
def cli():
    global guessGame, carGame
    guessGame = GuessingGame()
    carGame = CarGame()
    

@cli.command('greet')
@click.argument('name')
def greet(name):
    print("Hello ", name)

@cli.command('guessing-game')
def guess_game():
    """A game where you can guess a number"""
    guessGame.play()

@cli.command('car-game')
def car_game():
    carGame.start()

if __name__ == '__main__':
    cli()

