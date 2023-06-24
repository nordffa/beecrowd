resp_cor = int(input())
r1, r2, r3, r4, r5 = map(int, input().split())
lista = [r1, r2, r3, r4, r5]
qnts = sum(1 for v in lista if v == resp_cor)
print(qnts)
