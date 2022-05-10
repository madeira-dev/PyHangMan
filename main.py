from random import shuffle
from user_login import login

# variables
words = ["teclado", "cadeira", "mesa", "monitor", "computador"]
attempts = 0
attempts_count = 0
user_word = ""
user_letter = ""

# functions


def select_word(words):
    random_pos = shuffle(words)
    return random_pos[0]


def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


def reveal_letter(letter, word):
    for i in range(len(word)):
        if word[i] == letter:
            print(letter, end="")
        else:
            print("_", end="")


def check_full_word(user_word, word):
    if user_word == word:
        return True
    else:
        return False

# main


def main():
    word = select_word(words)

    while attempts_count <= attempts:
        user_letter = str(input("Enter a letter: "))

        if check_letter(user_letter, word):
            reveal_letter(user_letter, word)
        else:
            print("letter not in word")
            attempts_count += 1


if __name__ == "__main__":
    main()
