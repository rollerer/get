while 1>0:
    a=float(input('a-?'))
    b=float(input('b-?'))
    if a/b - b/(a-b) < 0.0001:
        print("Да")
    else:

        print('Нет')
