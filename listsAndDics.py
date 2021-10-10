def run():
    my_list = [1,'Hello', True, 4.5]
    dictionary = {'firstname':'Juan', 'lastname':'Alvarez'}

    super_list=[{'firstname':'Juan', 'lastname':'Alvarez'},
                {'firstname':'Pepo', 'lastname':'Perez'}  ]

    super_dict = {
        'natural-items': [1,2,3,4,5],
        'float-items': [0.3,0.2,0.3,0.4,0.5],
        'integer-items': [-2,-1,0,1,2]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for value in super_list:
        for key,value in value.items():
            print (f'{key}-{value}')

if __name__ == '__main__':
    run()