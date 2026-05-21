n = int(input('Digite um número: '))
print('=' * 30)
print('SEQUÊNCIA DE FIBONACCI'.center(30))
print('=' * 30)
t1 = 0
t2 = 1
print('0 -> ',end='')
for c in range(t1,n-1):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t1} -> ', end='')
print('FIM')

