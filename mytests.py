from main import *
import unittest
import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

# TODO: pensa em um teste melhor pra verificar o array aleatorio


def test_select_word(self):
    words = ["banana", "abacate", "laranja", "abacaxi"]
    random.shuffle(words)
    self.assertEqual(select_word(words), words, words)

# TODO: adicionar mais testes da funcao check_letter


def test_check_letter(self):
    self.assertEqual(check_letter("a", "banana"), True)
    self.assertEqual(check_letter("b", "banana"), True)


def test_add_letter(self):
    self.assertEqual(add_letter("a", "banana", ["_", "_", "_", "_", "_", "_"]), [
        "_", "a", "_", "a", "_", "a"])

# TODO: adicionar mais testes da funcao check_full_word


def test_check_full_word(self):
    self.assertEqual(check_full_word(
        "banana", "banana"), True)
    self.assertEqual(check_full_word("abacaxi", "abacate"), False)


# TODO: encontrar melhor forma de testar se conteudo do arquivo foi adicionado no array

'''
    def test_file_words_to_vector(self):
        words = open("words.txt", "r").read()
        words_vector = file_words_to_vector(words.split("\n"))
        self.assertEqual(
            words_vector, ["banana", "abacate", "laranja", "abacaxi"])
'''
