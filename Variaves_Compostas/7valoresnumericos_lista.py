numeros = [[],[]]
valor = 0
print('=' * 40)
print('VALORES'.center(40))
print('='*40)
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)


print('=' * 60)
print('RESULTADO'.center(60))
print('=' * 60)


numeros[0].sort()
print(f'Os números pares em ordem crescente foi: ',end='')
for p in numeros[0]:
    print(f' {p} ',end='')
print()

numeros[1].sort()
print(f'Os números impares em ordem crescente foi: ',end='')
for p in numeros[1]:
    print(f' {p} ',end='')
print()
