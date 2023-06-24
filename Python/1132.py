x, y, soma = int(input()), int(input()), 0
x, y = min(x, y), max(x, y)
for c in range(x, y+1):
    if c % 13 != 0:
        soma += c
print(soma)
