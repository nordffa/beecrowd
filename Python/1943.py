n = int(input())
if n == 1:
    print('Top 1')
elif n >= 2 and n <= 3:
    print('Top 3')
elif n >= 4 and n <= 5:
    print('Top 5')
elif n >= 6 and n <= 10:
    print('Top 10')
elif n >= 11 and n <= 25:
    print('Top 25')
elif n >= 26 and n <= 50:
    print('Top 50')
elif n >= 51 and n <= 100:
    print('Top 100')
