cont = soma = media = maior = menor = 0
usuario = 'S'
while usuario in 'S':
    print('-'*30)
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    usuario = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
media = soma / cont
print('='*40)
print(f'A media desses {cont} valores foi {media:.2f}')
print(f'O maior número digitado foi {maior} e o menor {menor}')
