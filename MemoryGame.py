import random
import tkinter as tk

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def start_game(self, seq):
        root = tk.Tk()
        root.title("Fun Game")
        tk.Label(root, text='   '.join(str(x) for x in seq), font=(None, 20), width=50, height=5).pack()
        root.after(1700, lambda: root.destroy())  # time in ms
        root.mainloop()

    def generate_sequence(self):
        seq = []
        for i in range(self.difficulty):
            seq.append(int(random.randint(1, 101)))
        return seq


    def get_list_from_user(self):
        while True:
          try:
            user_numbers = input(f'Enter the numbers you remember separated by space \n')
            user_seq = user_numbers.split()
            for i in range(0, len(user_seq)):
                user_seq[i] = int(user_seq[i])
            break
          except ValueError:
            print("Invalid input. Please try again!")
        return user_seq


    def is_list_equal(self, seq, user_seq):
        seq.sort()
        user_seq.sort()
        return user_seq == seq


    def play(self):
        print(f"\n\n WELCOME TO THE MEMORY GAME. TRY REMEMBERING THE FOLLOWING NUMBERS IN THE POPUP WINDOW.\n")

        seq = self.generate_sequence()
        self.start_game(seq)
        user_seq = self.get_list_from_user()
        user_result = self.is_list_equal(seq, user_seq)
        if user_result:
            print(f"YOU WON")
        else:
            print(f"YOU LOOSE!")
        return user_result

