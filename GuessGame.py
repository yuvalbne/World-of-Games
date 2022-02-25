import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
          try:
            user_number = int(input(f"Please enter a number between 1 to {self.difficulty}\n"))
            if user_number < 1 or user_number > self.difficulty:
              raise ValueError()
            break
          except ValueError:
            print("Invalid input. Please try again!")
        return user_number

    def compare_results(self, user_number ):
        return self.secret_number == user_number

    def play(self):
        print(f"\n\n WELCOME TO THE GUESS GAME.\n")
        self.generate_number()
        user_number = self.get_guess_from_user()
        user_result = self.compare_results(user_number)
        if user_result:
            print(f"YOU WON! MY NUMBER WAS ALSO {self.secret_number}")
        else:
            print(f"YOU LOOSE! MY NUMBER WAS {self.secret_number}")
        return self.compare_results(user_number)






