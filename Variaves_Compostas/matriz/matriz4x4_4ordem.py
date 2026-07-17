from random import randint
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
somadiag = maior = 0
produto = 1


for l in range(0,4):
    for c in range(0,4):
        matriz[l][c] = randint(1,20)
        #Soma da diagonal principal
        if l == c:
            somadiag += matriz[l][c]

#Mostrar a matriz
print('=' * 35)
print('MATRIZ'.center(35))
print('=' * 35)
for l in range(0,4):
    for c in range(0,4):
        print(f' [{matriz[l][c]:^5}] ',end='')
    print()


print('=' * 35)
print(f'A soma da diagonal principal foi {somadiag}')


#Multiplicar os valores da segunda linha
for c in range(0,4):
    produto *= matriz[1][c]
print(f'O produto entre os valores da segunda linha foi {produto}')


#Ver o maior valor da terceira coluna
for l in range(0,4):
    if matriz[l][2] > maior:
        maior = matriz[l][2]
print(f'O maior valor da terceira coluna foi {maior}')