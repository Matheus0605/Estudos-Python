import Utils
from random import choice

PATH_JSON = 'Projeto Forca/palavras.json'

dict_words = Utils.read_words(PATH_JSON=PATH_JSON)

hint, word = Utils.generate_words(dict_words=dict_words)

print(hint, word)

accept =[]
error = []
hint, word, error, accept = Utils.accept_error(word=word, accept=accept, error=error)



