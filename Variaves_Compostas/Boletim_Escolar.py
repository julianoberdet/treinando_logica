from time import sleep
ficha = []


print('=' * 40)
print('ESTATISTICAS DOS ALUNOS'.center(40))
print('=' * 40)


while True:
    print(f'Aluno {len(ficha) + 1}'.center(40))
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA1: '))
    nota2 = float(input('NOTA2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    print('-' * 40)


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('-' * 40)


print('=' * 40)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')


while True:
    opc = int(input('De qual aluno quer saber as notas?[999 interrompe] '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha)-1:
        print(f'As notas do aluno {ficha[opc][0]} foram {ficha[opc][1]}')


sleep(1)
print('Obrigado!! Volte sempre')