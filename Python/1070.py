x = int(input())
if x % 2 == 0:
    x1 = x + 1
    for seis in range (0, 12, 2):
        print(f'{x1 + seis}')
else:
    for seis in range (0, 12, 2):
        print(f'{x + seis}')