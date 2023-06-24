n, m = int(input()), int(input())
for c in range(0, 101):
    if (n + c) / 2 == m:
        print(c)
        break
