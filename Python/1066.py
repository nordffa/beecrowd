pos, neg, par, impar = 0, 0, 0, 0
for c in range(1, 6):
    num = int(input())
    if num > 0:
        pos += 1
    if num % 2 == 0:
        par += 1
    if num < 0:
        neg += 1
    if num % 2 == 1:
        impar += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
