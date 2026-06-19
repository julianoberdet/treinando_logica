def Fator(v):
    c = v
    r = 1
    print(f'{c}! =',end='')
    while True:
        r *= c
        print(f' {c} ',end='')
        c -= 1
        print('X' if c >= 1 else '= ',end='')
        if c < 1:
            break
    return r


n = int(input('Digite um número: '))
f = Fator(n)
print(f)