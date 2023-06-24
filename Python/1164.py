vezes = int(input())
for c in range(0, vezes):
    num = int(input())
    soma = 0
    for x in range(1, num):
        if num % x == 0:
            soma += x
    if soma == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')
