sexo = str(input('SEXO: ')).strip().upper()[0]
while sexo not in 'MF':
    print('\033[31mERRO! DIGITE A OPÇÃO CERTA\033[m')
    sexo = str(input('SEXO: ')).strip().upper()[0]
print(f'SEXO [{sexo}] REGISTRADO COM SUCESSO!')
