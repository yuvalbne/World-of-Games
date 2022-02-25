from Utils import SCORES_FILE_NAME
from os.path import exists


def add_score(difficulty):
    print(exists(SCORES_FILE_NAME))
    if exists(SCORES_FILE_NAME):
        score_until_now = get_score_from_file()
        score_until_now = int(get_score_from_file()) if score_until_now != '' else 0
        score_until_now = score_until_now +((difficulty * 3) + 5)
    else:
        score_until_now = 0
    write_score_to_file(score_until_now)


def get_score_from_file():
    file = open(SCORES_FILE_NAME, 'r')
    score = file.read()
    file.close()
    return score


def write_score_to_file(score_until_now):
    file = open(SCORES_FILE_NAME, 'w')
    file.write(str(score_until_now))
    file.close()
