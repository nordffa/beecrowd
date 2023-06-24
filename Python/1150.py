x = int(input())
while True:
    z = int(input())
    if z > x:
        break
valor_inicial = x
tentativas = 1
lista = [x]
while True:
    if sum(lista) > z:
        print(tentativas)
        break
    else:
        valor_inicial += 1
        tentativas += 1
        lista.append(valor_inicial)
