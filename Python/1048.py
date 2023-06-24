salario = float(input())
salario_novo, percentual = 0, 0
if 0 <= salario <= 400.00:
    salario_novo = salario + (salario * 0.15)
    percentual = 15
elif 400 < salario <= 800:
    salario_novo = salario + (salario * 0.12)
    percentual = 12
elif 800 < salario <= 1200:
    salario_novo = salario + (salario * 0.10)
    percentual = 10
elif 1200 < salario <= 2000:
    salario_novo = salario + (salario * 0.07)
    percentual = 7
elif salario > 2000:
    salario_novo = salario + (salario * 0.04)
    percentual = 4
print(f'Novo salario: {salario_novo:.2f}')
print(f'Reajuste ganho: {salario_novo - salario:.2f}')
print(f'Em percentual: {percentual} %')
