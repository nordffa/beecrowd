soma = contador = 0
while True:
    idade = int(input())
    if idade >= 0:
        soma += idade
        contador += 1
    else:
        break
print(f'{soma/contador:.2f}')
