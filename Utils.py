from os import system, name

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 400
GOOD_RETURN_CODE = 200


def screen_cleaner():
    system('cls' if name == 'nt' else 'clear')


