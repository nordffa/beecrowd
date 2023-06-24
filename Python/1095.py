i, j = 1, 60
print(f"I={i} J={j}")
while True:
    if j == 0:
        break
    else:
        i += 3
        j -= 5
        print(f"I={i} J={j}")
