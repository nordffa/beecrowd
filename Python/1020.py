idade = int(input())
anos, meses, dias = 0, 0, 0

while idade >= 365:
    idade -= 365
    anos += 1
while idade >= 30:
    idade -= 30
    meses += 1
if idade < 30:
    dias = idade

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
