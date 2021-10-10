import os
import random
from typing import Type

checked_letters = []

def check_letter(word_dict, input_letter):
    os.system("clear")
    print('ADIVINA LA PALABRA')
    try:
        if len(input_letter) == 1 and input_letter.isalpha():
            
                
                arr_word = list(word_dict.values())
                arr_word_set = list(set(arr_word)) #Función set para eliminar los valores el array repetidos

                if input_letter in arr_word and input_letter not in checked_letters: 
                        checked_letters.append(input_letter)
                print(arr_word)
                print(checked_letters)
                
                template = ' ' 
                for letter in arr_word:
                    if letter in checked_letters:
                        template += f' {letter} '
                    else:
                        template+= f' _ '
                print('Palabra: ',template)                    


                if len(checked_letters) == len(arr_word_set):
                        raise ValueError

                input_letter = input('Ingresa otra letra: ')
                check_letter(word_dict, input_letter)
        else:
            print('Solo puedes ingresar de a una letra')
            input_letter = input('Ingresa otra letra: ')
            check_letter(word_dict, input_letter)


    except ValueError:
        print('Ganaste!')



def run():
    palabras = []
    
    with open('./archivos/data.txt','r',encoding='utf-8') as f:
        for line in f:
            palabras.append(line)

    
    limite = len(palabras)
    rand = int(1+(limite-1)*random.random()) 
    enumerated_parsed_word = list(enumerate(palabras[rand]))

    last_Item = len(dict(enumerated_parsed_word)) - 1

    word_dict = dict(enumerated_parsed_word)
    word_dict.pop(last_Item)
    print(word_dict)

    space = ''
    for letter in list(word_dict.values()):
        space+= ' _ '

    print('Palabra: ',space)
    input_letter = input('Ingresa una letra: ')

    if input_letter.isalpha():
        check_letter(word_dict, input_letter)
    else:
        print('Ingresa solo letras')
        input_letter = input('Ingresa una letra: ')
        check_letter(word_dict, input_letter)
    
    

if __name__ == '__main__':
    os.system("clear")
    print('ADIVINA LA PALABRA\n\n')
    run()



    """ lenguajes = ["Java", "C", "C++", "Rust", "Elixir"]
    list(enumerate(lenguajes,1))
    print(list(enumerate(lenguajes,1)))

    dic ={
        'Pepo' : 13,
        'Papi' : 12,
        'Pepi' : 15,
    }

    pepi = dic.get('Pepi')
    print(pepi) """
################################