from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

def welcome(name):
    return f"Hello {name} and welcome to the World of Games.\nHere you can find many cool games to play"


# I added validations on user input - input can be only a number in the asked range.
def load_game():
    while True:
        try:
            game_to_play = int(input(f"Please choose a game to play:\n"
                                     + "1. Memory Game - a sequence of numbers will appear for "
                                     + "1 second and you have to guess it back\n"
                                     + "2. Guess Game - guess a number and see if you chose like the computer\n"
                                     + "3. Currency Roulette - try and guess the value of a "
                                     + "random amount of USD in ILS\n"))
            if game_to_play < 1 or game_to_play > 3:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please try again!")

    while True:
        try:
            difficulty = int(input(f"Please choose game difficulty from 1 to 5:\n"))
            if difficulty < 1 or difficulty > 5:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please try again!")

    match game_to_play:
        case 1:
            game_result = MemoryGame(difficulty).play()
        case 2:
            game_result = GuessGame(difficulty).play()
        case 3:
            game_result = CurrencyRouletteGame(difficulty).play()

    if game_result:
        add_score(difficulty)






