vezes = int(input())
soma = 0
for c in range(0, vezes):
    n1, n2 = map(int, input().split())
    resultado = n1 * n2
    soma += resultado
print(soma)
