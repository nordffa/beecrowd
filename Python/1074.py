vezes = int(input())
for repet in range(0, vezes):
    valor = int(input())
    if valor > 0:
        if valor % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif valor < 0:
        if valor % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    elif valor == 0:
        print('NULL')
