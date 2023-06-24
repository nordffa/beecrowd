A, B, C = map(float, input().split())
lista = [A, B, C]
ordem = sorted(lista, reverse=True)
if ordem[0] >= (ordem[1] + ordem[2]):
    print('NAO FORMA TRIANGULO')
else:
    if ordem[0] ** 2 == (ordem[1] ** 2 + ordem[2] ** 2):
        print('TRIANGULO RETANGULO')
    if ordem[0] ** 2 > (ordem[1] ** 2 + ordem[2] ** 2):
        print('TRIANGULO OBTUSANGULO')
    if ordem[0] ** 2 < (ordem[1] ** 2 + ordem[2] ** 2):
        print('TRIANGULO ACUTANGULO')
    if A == B and B == C:
        print('TRIANGULO EQUILATERO')
    if A == B and A != C or A == C and A != B:
        print('TRIANGULO ISOSCELES')
