valor = int(input())
vr = valor
nota100, nota50, nota20, nota10, nota5, nota2, nota1 = 0, 0, 0, 0, 0, 0, 0

while vr >= 100:
    vr -= 100
    nota100 += 1
while vr >= 50:
    vr -= 50
    nota50 += 1
while vr >= 20:
    vr -= 20
    nota20 += 1
while vr >= 10:
    vr -= 10
    nota10 += 1
while vr >= 5:
    vr -= 5
    nota5 += 1
while vr >= 2:
    vr -= 2
    nota2 += 1
if vr == 1:
    nota1 += 1

print(valor)
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')
