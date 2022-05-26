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


def add_letter(letter, word, user_word):
    for i in range(len(word)):
        if word[i] == letter:
            user_word[i] = letter
    return user_word


def check_full_word(user_word, word):
    if user_word == word:
        return True
    else:
        return False


def file_words_to_vector(words):
    words_vector = []
    for word in words:
        words_vector.append(word.strip())
    return words_vector


def main():

    # utilizando componente reutilizavel para login
    print("insira o nome de usuário:")
    username = input()
    print("insira a senha:")
    password = input()

    user = user_login.login(username, password)

    if user.check_login():
        print("Bem vindo!")
    else:
        print("Usuário ou senha inválidos!")
        return
    ###

    words = open("words.txt", "r").read()
    words_vector = file_words_to_vector(words.split("\n"))

    word = select_word(words_vector)[0]
    user_word = ["_" for i in range(len(word))]

    letters_found = 0

    attempts = len(word) // 2
    attempts_count = 0

    print("\nTotal de erros permitidos: ", attempts)

    while attempts_count <= attempts:
        print("\nErros cometidos: ", attempts_count)

        print("\nPalavra: ", end="")
        print(user_word)

        if len(word) - letters_found > len(word) // 2:
            user_letter = input("\nDigite uma letra: ")

            if check_letter(user_letter, word):
                user_word = add_letter(user_letter, word, user_word)
                letters_found += 1
            else:
                print(".Letra não encontrada")
                attempts_count += 1
                if attempts_count == attempts:
                    print(".Número máximo de tentativas atingido\n.Você perdeu!")
                    break

        if len(word) - letters_found == len(word) // 2:
            print("\nPalavra: ", end="")
            print(user_word)

            print("falta menos da metade das letras, agora chuta a palavra inteira")
            user_word = input("digite a palavra: ")

            if len(user_word) == 1:
                print("agr nao pode chutar letra, só a palavra inteira")
                user_word = input("digite a palavra: ")

            if check_full_word(user_word, word):
                print("Boa, você acertou a palavra")
                break

            else:
                print("Você errou, a palavra era:", word)
                break


if __name__ == "__main__":
    main()
