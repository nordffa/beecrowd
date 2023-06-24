c = 0
t = 0
for cont in range(1, 7):
    num = float(input())
    if num > 0:
        c += 1
        t += num
print(f'{c} valores positivos')
print(f'{t / c:.1f}')
