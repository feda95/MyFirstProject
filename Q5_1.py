def exchange_values():
    DicList = {'blue': '0000FF', 'white': '00FF00', 'black': 'FFFF00', 'yellow': 'FF0000', 'green': 'FFFFFF',
               'red': '000000'}

    print(DicList.items())

    x = DicList['blue'], ['white']
    print(x)
    y = DicList.keys()
    print(y)
    y = DicList.values()
    print(y)

    lista = ['blue', 'white', 'black', 'yellow', 'green', 'red']


exchange_values()

