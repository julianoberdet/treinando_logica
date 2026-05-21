from random import randint
print('='*40)
print('JOGO DO PAR OU IMPAR'.center(40))
print('='*40)
v = 0


while True:
    usuario = int(input('Escolha um número: '))
    pc = randint(0, 10)
    soma = usuario + pc


    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('PAR ou IMPAR? ')).strip().upper()[0]
    print(f'Você jogou {usuario} e o pc jogou {pc} e deu {soma} -> ',end='')


    if escolha in 'P':
        if soma % 2 == 0:
            print('Deu PAR, \033[32mVOCÊ GANHOU\033[m')
            v += 1
        else:
            print('Deu IMPAR, \033[31mVOCÊ PERDEU\033[m')
            break
    elif escolha in 'I':
        if soma % 2 == 1:
            print('Deu IMPAR,\033[32mVOCÊ GANHOU\033[m')
            v += 1
        else:
            print('Deu PAR, \033[31mVOCÊ PERDEU\033[m')
            break
    print('Vamos jogar novamente')
    print('=' * 35)


print('-'*30)
print(f'Você teve o total de {v} vitórias',end='')



