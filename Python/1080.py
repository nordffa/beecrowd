maior = pos = 0
for c in range(1, 101):
    valor = int(input())
    if valor > maior:
        maior = valor
        pos = c
print(maior)
print(pos)
