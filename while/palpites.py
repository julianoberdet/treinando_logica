palpites = 0
from random import randint
pc = randint(0,10)
acertou = False
print('\033[34;40m=\033[m'*51)
print('\033[34;40m---------------Jogo de advinhações-----------------\033[m'.center(51))
print('\033[34;40m=\033[m'*51)
print('\033[32;40mSou seu PC, acabei de pensar em um número de 0 à 10\033[m')
print('\033[32;40mTente acertar...                                   \033[m')
print('\033[32;40m=\033[m'*51)
while not acertou:
    eu = int(input('\033[30;1;46mDigite seu palpite de 0 à 10 ->\033[m '))
    palpites += 1
    if eu == pc:
        acertou = True
    else:
        if pc > eu:
            print('\033[30;1;42mMAIS... TENTE NOVAMENTE        \033[m')
            print()
        else:
            print('\033[30;1;41mMENOS... TENTE NOVAMENTE       \033[m')
            print()
print(f'\033[30;1;43mO Computador pensou no número {pc}\033[m')
print()
print(f'\033[32;1;40mVocê acertou com {palpites} tentativas, Parabéns!\033[m')



#JEITO QUE EU FIZ
'''
jogadas = 0
from random import randint
from time import sleep
pc = randint(0, 10)
print('='*30)
print('Jogo de advinhações'.center(30))
print('='*30)
print('Vou pensar em um número e você vai tentar advinhar.')
sleep(1)
print()
print('-'*30)
eu = int(input('Qual número pensei[DE 0 a 10]? '))
print('='*30)
print(f'Você digitou o número {eu} e',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('. ',end='')
sleep(0.5)
while eu != pc:
    jogadas += 1
    print(f'\033[31mERROU!Tente novamente\033[m')
    eu = int(input('Qual número pensei[DE 0 a 10]? '))
    print('=' * 30)
    print(f'Você digitou o número {eu} e', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('. ', end='')
    sleep(0.5)
    if eu == pc:
        print(f'\033[32mACERTOU!\033[m pensei no número {pc}')
        jogadas += 1
print(f'Você Jogou {jogadas} vezes para conseguir advinhar')'''
