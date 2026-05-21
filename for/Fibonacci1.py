print('-' * 40)
print('Sequência de Fibonacci'.center(40))
print('-' * 40)
T1 = 0
T2 = 1
print(f'{T1} {T2}',end='')
for C in range(3,16):
    T3 = T1 + T2
    print(f' {T3}',end='')
    T1 = T2
    T2 = T3
    C += 1
print()
print('-'*40)