A, B, C = map(float, input().split())
area = (A * C) / 2
areac = 3.14159 * C**2
areat = (A + B) * C / 2
areaq = B * B
arear = A * B
print(f'TRIANGULO: {area:.3f}')
print(f'CIRCULO: {areac:.3f}')
print(f'TRAPEZIO: {areat:.3f}')
print(f'QUADRADO: {areaq:.3f}')
print(f'RETANGULO: {arear:.3f}')
