cod, qtd, val = map(float, input().split())
cod2, qtd2, val2 = map(float, input().split())
vt1, vt2 = qtd * val, qtd2 * val2
vf = vt1 + vt2
print(f'VALOR A PAGAR: R$ {vf:.2f}')
