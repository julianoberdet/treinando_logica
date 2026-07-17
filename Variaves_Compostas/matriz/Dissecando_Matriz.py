from time import sleep
matriz = [[0] * 4 for _ in range(4)]
def opcao():
    print('''[1] Mostrar Matriz
[2] Diagonal Principal
[3] Triângulo Superior
[4] Triângulo Inferior
[5] Sair''')


def opc1():
    for l in range(0, 4):
        for c in range(0, 4):
            print(f'{matriz[l][c]:^5}', end='')
        print()


def opc2():
        for l in range(0,4):
            for c in range(0,4):
                if l == c:
                    print(f'{matriz[l][c]:^5}',end='')
                else:
                    print(' ' * 5,end='')
            print()


def opc3():
        for l in range(0,4):
            for c in range(0,4):
                if c > l:  # acima da diagonal
                    print(f'{matriz[l][c]:^5}', end='')
                else:
                    print(' ' * 5, end='')
            print()


def opc4():
        for l in range(4):
            for c in range(4):
                if l > c:  # abaixo da diagonal
                    print(f'{matriz[l][c]:^5}', end='')
                else:
                    print(' ' * 5, end='')
            print()



for l in range(4):
    for c in range(4):
        while True:
            try:
                matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
                break
            except ValueError:
                print('Digite um valor correto.')
            except KeyboardInterrupt:
                print('\nO usuário não digitou nada.')
                exit()


print(' MENU DE OPÇÕES '.center(40))
print('=' * 40)
while True:
    opcao()
    try:
        while True:
            opc = int(input('=========> opção: '))
            break
        if opc == 1:
            print('\nMatriz inteira\n')
            opc1()
        elif opc == 2:
            print('\nDiagonal Principal\n')
            opc2()
        elif opc == 3:
            print('\nTriângulo Superior\n')
            opc3()
        elif opc == 4:
            print('\nTriângulo Inferior\n')
            opc4()
        elif opc == 5:
            print('ENCERRANDO...')
            break
        else:
            print('ERRO! digite uma opção correta')
    except ValueError:
        print('Digite uma opção válida')
    except KeyboardInterrupt:
        print('O usuário prefiriu não informar opção')
        exit()
    print('=' * 30)
sleep(2)
print('Muito obrigado!!')

