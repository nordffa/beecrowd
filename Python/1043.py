A, B, C = map(float, input().split())
medidas = [A, B, C]
ordem = sorted(medidas)
if ordem[0] + ordem[1] > ordem[2]:
    print(f'Perimetro = {A + B + C:.1f}')
else:
    print(f'Area = {(A + B) * C / 2:.1f}')
