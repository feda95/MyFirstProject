lista = ['blue', 'white', 'black', 'yellow', 'green', 'red', 'red']


def exchange_values(lista):
    DicList = {'blue': '0000FF', 'white': '00FF00', 'black': 'FFFF00', 'yellow': 'FF0000', 'green': 'FFFFFF',
               'red': '000000'}

    for index, list in enumerate(lista):
        lista[index] = DicList[lista[index]]
    print(lista)


exchange_values(lista)

