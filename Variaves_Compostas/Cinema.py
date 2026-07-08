import os

cadeiras = ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10']

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostra_fileira():
    for cadeira in cadeiras:
        print(f'[ {cadeira:^3} ]', end=' ')
    print()
    print('-' * 70)

while True:
    limpa_tela()
    mostra_fileira()

    reserva = input('Reservar a cadeira: ').strip().upper()

    if reserva in cadeiras:
        indice = cadeiras.index(reserva)
        cadeiras[indice] = '---'
        print(f'Cadeira {reserva} RESERVADA!')
    elif reserva.startswith('B') and reserva[1:].isdigit():
        print('ERRO: Lugar ocupado!')
    else:
        print('ERRO: Cadeira inexistente!')

    outra = input('Quer reservar outra? [S/N] ').strip().upper()[0]
    if outra == 'N':
        break

limpa_tela()
print('RESERVAS FINALIZADAS!\n')
mostra_fileira()
print('Obrigado por utilizar o sistema!')