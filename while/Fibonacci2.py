V = int(input('Quantos termos você quer? '))
T1 = 0
T2 = 1
print(f'{T1} {T2}',end='')
C = 2
while C < V:
    T3 = T1 + T2
    print(f' {T3}', end='')
    T1 = T2
    T2 = T3
    C += 1