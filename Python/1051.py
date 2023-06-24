renda = float(input())
if renda <= 2000:
    print('Isento')
elif 2000 < renda <= 3000:
    ir = (renda - 2000) * 0.08
    print(f'R$ {ir:.2f}')
elif 3000 < renda <= 4500:
    v1 = renda - 3000
    ir = (v1 * 0.18) + 80
    print(f'R$ {ir:.2f}')
elif renda > 4500:
    v1 = renda - 4500
    ir = (v1 * 0.28) + 350
    print(f'R$ {ir:.2f}')
