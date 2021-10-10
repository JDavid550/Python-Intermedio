def read():
    number = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            number.append(int(line))
    print(number)

def write():
    names = ['Pepe', 'Facho', 'Pepito']
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")



def run():
    write()

if __name__ == '__main__':
    run()