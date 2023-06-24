hi, hf = map(int, input().split())
if hi <= 24 and hf <= 24:
    if hi > 12 and hf < 12:
        hi = 24 - hi
        ht = hi + hf
        print(f'O JOGO DUROU {ht} HORA(S)')
    elif hi < 12 and hf > 12:
        ht = hf - hi
        print(f'O JOGO DUROU {ht} HORA(S)')
    if hi == hf:
        ht = 24
        print(f'O JOGO DUROU {ht} HORA(S)')
