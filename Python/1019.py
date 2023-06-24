tempo = int(input())
horas, minutos, segundos = 0, 0, 0

while tempo >= 3600:
    tempo -= 3600
    horas += 1
while tempo >= 60:
    tempo -= 60
    minutos += 1
if tempo < 60:
    segundos = tempo

print(f'{horas}:{minutos}:{segundos}')
