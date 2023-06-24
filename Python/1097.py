v1, v2 = 7, 4
for x in range(1, 10, 2):
    for c in range(v1, v2, -1):
        print(f'I={x} J={c}')
    v1 += 2
    v2 += 2
    