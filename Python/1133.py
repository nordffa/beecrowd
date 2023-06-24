valores = []
for y in range(0, 2):
    valor = int(input())
    valores.append(valor)
valores.sort()
for c in range(valores[0]+1, valores[1]):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
