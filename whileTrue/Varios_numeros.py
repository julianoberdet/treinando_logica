qtd = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    qtd += 1
print(f'A soma de {qtd} valores foi {soma}')
