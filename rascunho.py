maior18 = homens = mulher20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: ')).upper().strip()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'São {maior18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'São {mulher20} mulheres com menos de 20 anos')









