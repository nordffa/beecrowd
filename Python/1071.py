x, y = int(input()), int(input())
soma = 0
if y < x:
    for c in range(x-1, y, -1):
        if c % 2 == 1:
            soma += c
else:
    for c in range(x-1, y):
        if c % 2 == 1:
            soma += c
print(soma)
