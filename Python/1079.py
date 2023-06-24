n = int(input())
for _ in range(0, n):
    v1, v2, v3 = map(float, input().split())
    mp = ((v1*2)+(v2*3)+(v3*5))/10
    print(f'{mp:.1f}')
