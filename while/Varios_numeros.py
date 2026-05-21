n = tot = soma = 0
while n != 999:
    print('-' * 30)
    n = int(input('Digite um número: '))
    if n != 999:
        tot += 1
        soma += n
print('-'*30)
print('SAINDO...'.center(30))
print('-'*30)
print(f'Foram digitados {tot} números, e a soma entre os números foi {soma}')