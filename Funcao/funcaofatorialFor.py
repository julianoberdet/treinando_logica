def Fator(v):
    res = 1
    print(f'{v}! =',end='')
    for c in range(v,0,-1):
        res *= c
        print(f' {c} ', end='')
        print('X' if c > 1 else '= ', end='')
    return res


n = int(input('Digite um número: '))
r = Fator(n)
print(r)

