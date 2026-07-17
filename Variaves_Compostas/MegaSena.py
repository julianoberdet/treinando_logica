from random import randint
from time import sleep

print('=' * 30)
print('MEGA SENA'.center(30))
print('=' * 30)

#Tratamento de erro
while True:
    try:
        quant = int(input('Quantos jogos serão gerados? '))
        break
    except ValueError:
        print('Digite um valor certo.')
    except KeyboardInterrupt:
        print('O usuário prefiriu não informar valores')
        exit()

lista = []
jogos = []

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1

print()
print('='*7, f'SORTEANDO {quant} JOGOS', '=' * 7)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1} - {l}')
    sleep(1)
print('=' * 8, f' < BOA SORTE > ', '=' * 8)
