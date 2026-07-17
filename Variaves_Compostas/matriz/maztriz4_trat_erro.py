matriz = [[0, 0, 0] for _ in range(3)]

soma_pares = 0
soma_terceira_coluna = 0

# Leitura da matriz
for l in range(3):
    for c in range(3):
        while True:
            try:
                valor = int(input(f'Digite um valor para [{l}, {c}]: '))
                matriz[l][c] = valor

                # Soma dos pares
                if valor % 2 == 0:
                    soma_pares += valor

                # Soma da terceira coluna
                if c == 2:
                    soma_terceira_coluna += valor

                break

            except ValueError:
                print('Digite um número inteiro válido.')

            except KeyboardInterrupt:
                print('\nPrograma encerrado pelo usuário.')
                exit()

# Exibição da matriz
print('-' * 30)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()
print('-' * 30)

# Maior da segunda linha
maior_segunda_linha = matriz[1][0]
for c in range(1, 3):
    if matriz[1][c] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][c]

# Menor da primeira linha
menor_primeira_linha = matriz[0][0]
for c in range(1, 3):
    if matriz[0][c] < menor_primeira_linha:
        menor_primeira_linha = matriz[0][c]

print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_segunda_linha}.')
print(f'O menor valor da primeira linha é {menor_primeira_linha}.')