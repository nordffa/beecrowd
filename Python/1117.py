notas = []
while True:
    if len(notas) == 2:
        break
    else:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print('nota invalida')
print(f'media = {sum(notas)/2}')
