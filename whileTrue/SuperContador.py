from time import sleep
c = 1
while True:
        print('='*30)
        print('MENU'.center(30))
        print('='*30)
        print('''| [1] De 1 a 10              |
| [2] De 10 a 1              |
| [3] Para sair              |''')
        print('='*30)
        op = int(input('Qual opção? '))
        if op == 1:
            while c <= 10:
                print(f'{c}..',end='')
                c += 1
        if op == 2:
            for c in range(10,0,-1):
                print(f'{c}..',end='')
                c -= 1
        if op == 3:
            print('\033[31;40m   SAINDO...   \033[m'.center(40))
            sleep(1)
            print('\033[32;40m<< OBRIGADO! >>\033[m'.center(40))
            print('-' * 30)
            break
        if op < 1 or op > 3:
            print('\033[31mERRO! Digite uma opção válida...\033[m')
        print()