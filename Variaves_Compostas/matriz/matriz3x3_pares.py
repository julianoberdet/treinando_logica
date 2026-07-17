matriz = [[0,0,0],[0,0,0],[0,0,0]]
totpar = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor na posição {[l,c]}: '))

print('-' * 30)
print('''VERDE = PAR
VERMELHO = IMPAR''')
print('-' * 30)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            print(f' [\033[32m{matriz[l][c]:^5}\033[m] ',end='')
            totpar += 1
        else:
            print(f' [\033[31m{matriz[l][c]:^5}\033[m] ',end='')
    print()
print('-' * 30)
print(f'Ao todo são {totpar} números pares')