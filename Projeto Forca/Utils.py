def read_words(PATH_JSON):

    import json

    with open(PATH_JSON, mode='r', encoding='utf-8') as file:
        dictionary_words = json.load(file)

    return dictionary_words

def generate_words(dict_words):
    from random import choice

    list_hints = list(dict_words.keys())
    hint = choice(list_hints)
    word_key = choice(dict_words[hint])

    return hint, word_key

def accept_error(word, accept, error):

    human = 6

    while human > 0:

        user_input = str(input('Letra: ')).upper()
        if user_input.upper() in word.upper():

            if user_input in accept:

                print('Voce ja digitou essa letra')

            else:

                accept.append(user_input)
                print('entrou1')

            print('entrou2')

        else:
            
            if user_input.upper() in error:

                print('Voce ja digitou essa letra')  

            else: 
                    
                human -= 1
                error.append(user_input)
                print('ERRO', human)
    
    return word, accept, error