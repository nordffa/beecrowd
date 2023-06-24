notas = []
while True:
    if len(notas) < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print('nota invalida')
    elif len(notas) == 2:
        print(f'media = {sum(notas)/2:.2f}')
        notas.clear()
        print('novo calculo (1-sim 2-nao)')
        perg = int(input())
        while perg < 1 or perg > 2:
            print('novo calculo (1-sim 2-nao)')
            perg = int(input())
        if perg == 2:
            break
