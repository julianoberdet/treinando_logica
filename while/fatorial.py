n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
print(f' {c}! =',end='')
while c > 0:
    print(f' {c} ',end='')
    print('x' if c > 1 else '=',end='')
    f *= c
    c -= 1
print(f' {f}',end='')
