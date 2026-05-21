print('='*40)
print('SEQUÊNCIA DE FIBONACCI'.center(40))
print('='*40)
V = int(input('Quantos termos você quer? '))
C = 2
while True:
    if V <= 1:
        print(' 0', end='')
        C += 1
    elif V == 2:
        print(' 0 -> 1',end='')
        C += 1
    else:
        T1 = 0
        T2 = 1
        print(f'{T1} -> {T2}',end='')
        C = 3
        while True:
            T3 = T1 + T2
            print(f' -> {T3}',end='')
            T1 = T2
            T2 = T3
            C += 1
            if C > V:
                break
    if C > V:
        break