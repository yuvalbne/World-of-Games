import random
from currency_converter import CurrencyConverter

class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def random_number_for_use_guest(self):
        secret_number = random.randint(1, 100)
        return secret_number

    def get_money_interval(self, secret_number):
        amount_in_ils = CurrencyConverter().convert(secret_number, 'USD', 'ILS')
        bottom_interval = (amount_in_ils - (5 - self.difficulty))
        upper_interval = (amount_in_ils + (5 - self.difficulty))
        return bottom_interval, upper_interval


    def get_guess_from_user(self, secret_number):
        while True:
          try:
            user_guest = int(input(f'Guess how much is {secret_number}$ is in ILS? \n'))
            break
          except ValueError:
            print("Invalid input. Please try again!")
        return user_guest


    def is_user_won(self, user_guest, bottom_interval, upper_interval):
        return user_guest > bottom_interval and user_guest < upper_interval


    def play(self):
        print(f"\n\n WELCOME TO THE CURRENCY ROULETTE GAME.\n")
        secret_number = self.random_number_for_use_guest()
        bottom_interval, upper_interval = self.get_money_interval(secret_number)
        user_guest = self.get_guess_from_user(secret_number)
        user_result = self.is_user_won(user_guest, bottom_interval, upper_interval)
        if user_result:
            print(f"YOU WON! THE INTERVAL WAS BETWEEN {bottom_interval} - {upper_interval}  ")
        else:
            print(f"YOU LOOSE! THE INTERVAL WAS BETWEEN {bottom_interval} - {upper_interval} ")
        return user_result
