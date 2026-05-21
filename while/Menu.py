from time import sleep
escolha = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while escolha != 5:
    print('=' * 30)
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    print('=' * 30)
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
        print(f'O resutado da soma foi {resultado}')
    elif escolha == 2:
        resultado = n1 * n2
        print(f'{n1} x {n2} = {resultado}')
        print(f'O resultado da multiplicação foi {resultado}')
    elif escolha == 3:
        if n1 > n2:
            print(f'entre {n1} e {n2}, o maior é o {n1}')
        elif n2 > n1:
            print(f'entre {n1} e {n2}, o maior é o {n2}')
        else:
            print(f'Os números digitados são iguais')
    elif escolha == 4:
        print('-'*30)
        print('VAMOS COMEÇAR NOVAMENTE...')
        print('-'*30)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Saindo',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.')
        sleep(2)
        print('ATÉ ',end='')
        sleep(0.5)
        print('A ',end='')
        sleep(0.2)
        print('PRÓXIMA',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('-'*30)
        sleep(0.5)
    else:
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
