def eh_primo(n):
    lista = []
    for c in range(1, n+1):
        if n % c == 0:
            lista.append(c)
    if len(lista) == 2:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')


n = int(input())
for c in range(0, n):
    x = int(input())
    eh_primo(x)
