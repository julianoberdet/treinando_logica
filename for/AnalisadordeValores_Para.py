print('='*40)
print('ANALISADOR DE VALORES'.center(40))
print('='*40)
Soma = qtd5 = media = NUL = SPar = 0
for c in range(1,6):
    try:
         V = int(input(f'Digite o {c}º valor: '))
    except ValueError:
        print('\033[1;31mERRO!Digite um valor válido\033[m')
        V = int(input(f'Digite o {c}º valor: '))
    Soma += V
    media = Soma / c
    if V % 5 == 0:
        qtd5 += 1
    if V == 0:
        NUL += 1
    if V % 2 == 0:
        SPar += V
print('='*40)
print(f'A soma de todos os valores é {Soma}')
print(f'A média dos valores digitados é {media}')
print(f'Valores divisiveis por cinco: {qtd5}')
print(f'Valores nulos: {NUL}')
print(f'A somados valores pares é {SPar}')
print('='*40)
