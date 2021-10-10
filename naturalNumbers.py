#Listas comprimidas

from typing import Sequence


def run():

    squares = []
    for i in range(0,101):
        if i%3 != 0:
            squares.append(i**2)

    squares2 = [i**2 for i in range(0,101) if i%3 != 0] #Lista comprimida

    x = [i for i in range(0,100000) if i%4 == 0 if i%6==0 if i%9==0 ] #Reto de la clase
    print(x)


if __name__ == '__main__':
    run()