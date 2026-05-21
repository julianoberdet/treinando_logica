primeiro_termo = int(input('Primeiro termo: '))
razao_pa = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(f'{primeiro_termo} -> ',end='')
    c += 1
    primeiro_termo += razao_pa
print('FIM',end='')