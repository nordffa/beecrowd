n1, n2, n3, n4 = map(float, input().split())
p1, p2, p3, p4 = 2, 3, 4, 1
mp = ((n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)) / (p1 + p2 + p3 + p4)

if mp >= 7.0:
    print(f'Media: {mp:.1f}')
    print('Aluno aprovado.')
elif mp < 5.0:
    print(f'Media: {mp:.1f}')
    print('Aluno reprovado.')
elif mp >= 5.0 and mp <= 6.9:
    ne = float(input())
    print(f'Media: {mp:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {ne:.1f}')
    mf = (mp + ne) / 2
    if mf >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {mf:.1f}')
