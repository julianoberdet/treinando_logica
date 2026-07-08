matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somacol = maior = 0

# Perguntar ao usuario os números
for l in range(0, 3):
    for c in range(0, 3):
        while True:
            try:
                matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
                break
            except ValueError:
                print('Digite um número inteiro válido.')
            except KeyboardInterrupt:
                print('O usuario preferiu sair')

# Mostrar a matriz
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        # Calcular os pares de toda a matriz
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-' * 30)
print(f'A soma dos valores pares da matriz foi {par}')

# Somando a terceira coluna
for c in range(0, 3):
    somacol += matriz[c][2]
print(f'A soma dos valores da terceira coluna foi {somacol}')

# Vendo qual é o maior da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')