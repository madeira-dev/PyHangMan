import random
import login


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


# def login_credentials():
#     username = input("insira o nome de usuário:")
#     password = input("insira a senha:")
#     return username, password


def main():

    # utilizando componente reutilizavel para login
    print("Ja possui conta?")
    print("1 - Sim")
    print("2 - Nao")
    user_option = int(input("Digite a opcao: "))

    if user_option == 1:
        username = input("Insira o nome de usuário: ")
        password = input("Insira a senha: ")

        if login.user_login.check_login(username, password):
            print("Logado com sucesso!")
        else:
            print("Usuário ou senha incorretos!")

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
                    print("Você errou, a palavra era:", word)
                    break

        if len(word) - letters_found == len(word) // 2:
            print("\nPalavra: ", end="")
            print(user_word)

            print("falta menos da metade das letras, agora chuta a palavra inteira")
            while (1):
                user_word = input("digite a palavra: ")

                if len(user_word) == 1:
                    print("agora nao pode chutar letra, só a palavra inteira")

                if len(user_word) > 1:
                    print("teste")
                    if check_full_word(user_word, word):
                        flag = 1
                        print("Boa, você acertou a palavra")
                        break
                    else:
                        flag = 0
                        print("Você errou, a palavra era:", word)
                        break

            if (flag or not flag):
                break


if __name__ == "__main__":
    main()
