lista = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    #Ver se é par ou impar
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    #Ver se quer continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break


print('-' * 40)
print(f'A lista ficou assim',end='')
for c in lista:
    print(f' -> {c}',end='')
print()

print(f'Os pares foram',end='')
for c in par:
    print(f' -> {c}',end='')
print()

print(f'Os impares foram',end='')
for c in impar:
    print(f' -> {c}',end='')