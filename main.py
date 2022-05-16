import random
import user_login


def select_word(words):
    random.shuffle(words)
    return words


def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


<<<<<<< HEAD
def reveal_letter(letter, word, letters_found):
    for i in range(len(word)):
        if word[i] == letter:
            letters_found += 1
=======
def reveal_letter(letter, word, user_word, letters_found):
    print("\nPalavra: ", end="")
    for i in range(len(word)):
        if word[i] == letter:
>>>>>>> 1a8f2063ea9fa2fc3f4fa16a932c09ad364efd3d
            print(letter, end="")
            letters_found += 1

        else:
            print("_ ", end="")


# def add_letter(letter, word, user_word):
#     for i in range(len(word)):
#         if word[i] == letter:
#             user_word[i] = letter
#             return user_word


def check_full_word(user_word, word):
    if user_word == word:
        return True
    else:
        return False


def main():
    words = ["teclado", "cadeira", "mesa", "monitor", "computador"]
    word = select_word(words)[0]
    user_word = ""

    letters_found = 0

    attempts = len(word) // 2
    attempts_count = 0

    print("\nTotal de erros permitidos: ", attempts)

    while attempts_count < attempts:
        print("Erros cometidos: ", attempts_count)
        print("\nPalavra: ", end="")

        for letters in word:
            print("_ ", end="")

        if len(word) - letters_found > 4:
            user_letter = input("\nDigite uma letra: ")

            if check_letter(user_letter, word):
<<<<<<< HEAD
                reveal_letter(user_letter, word, letters_found)
=======
                reveal_letter(user_letter, word, user_word, letters_found)
>>>>>>> 1a8f2063ea9fa2fc3f4fa16a932c09ad364efd3d
            else:
                print("Letra não encontrada")
                attempts_count += 1
                if attempts_count == attempts:
                    print("\nVocê perdeu!")

        if len(word) - letters_found == len(word) // 2:
            print("agr só faltam 4 letras, chuta a palavra inteira")
            user_word = input("digite a palavra: ")

            if len(user_word) == 1:
                print("agr n pode chutar letra, só a palavra inteira")

            if check_full_word(user_word, word):
                print("Boa, você acertou a palavra")

            else:
                print("Você errou, a palavra era:", word)
                break


if __name__ == "__main__":
    main()
