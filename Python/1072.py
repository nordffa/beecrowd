repet = int(input())
vin = vout = 0

for num in range(0, repet):
    valor = int(input())
    if valor >= 10 and valor <= 20:
        vin += 1
    else:
        vout += 1

print(f'{vin} in')
print(f'{vout} out')
