A, B = map(int, input().split())
lista = [A, B]
ordem = sorted(lista)
if ordem[1] % ordem[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
