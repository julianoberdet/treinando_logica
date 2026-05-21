maior18 = mulher = homens = 0

while True:
        print('-' * 30)
        idade = int(input('IDADE: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('SEXO: ')).upper().strip()[0]
        if idade > 18:
            maior18 += 1
        if sexo in 'M':
            homens += 1
        if sexo in 'F' and idade < 20:
            mulher += 1

        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if resp == 'N':
            break

print(f'Foram cadastradas {maior18} pessoas maiores de 18 anos')
print(f'São {homens} homens cadastrados')
print(f'São {mulher} mulheres com menos de 20 anos')