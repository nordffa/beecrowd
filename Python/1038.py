esc, qtd = map(int, input().split())
match esc:
    case 1:
        total = qtd * 4.00
        print(f'Total: R$ {total:.2f}')
    case 2:
        total = qtd * 4.50
        print(f'Total: R$ {total:.2f}')
    case 3:
        total = qtd * 5.00
        print(f'Total: R$ {total:.2f}')
    case 4:
        total = qtd * 2.00
        print(f'Total: R$ {total:.2f}')
    case 5:
        total = qtd * 1.50
        print(f'Total: R$ {total:.2f}')

