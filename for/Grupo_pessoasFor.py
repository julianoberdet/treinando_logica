media = somaidade = maior_idade = mulher = 0
Homemvelho = ''
print('='*30)
print('\033[32m    ANAlISADOR DE PESSOAS\033[m')
print('='*30)
for c in range(1,5):
    print(f'{c}ª PESSOA'.center(30))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    print('-'*30)
    if sexo in 'Mm':
        if c == 1:
            Homemvelho = nome
            maior_idade = idade
        else:
            if idade > maior_idade:
                Homemvelho = nome
                maior_idade = idade
    if sexo in 'Ff':
        if idade < 20:
            mulher += 1
    somaidade += idade
    media = somaidade / c
print(f'O homem mais velho foi o {Homemvelho} com {maior_idade} anos')
print(f'No total: {mulher} mulher com menos de 20 anos')
print(f'A média de idade do grupo é {media}')