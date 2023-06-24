a = g = d = 0
while True:
        posto = int(input())
        if posto == 1:
            a += 1
        if posto == 2:
            g += 1
        if posto == 3:
            d += 1
        if posto == 4:
            break
print('MUITO OBRIGADO')
print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')
