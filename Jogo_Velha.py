def jogo(matriz):
    for l in range(3):
        for c in range(3):
            print(f'| {matriz[l][c]:^5} ', end='')
        print('|')
        if l < 2:
            print('--------|-------|--------')


def limpa_tela():
    print('\n' * 50)


def jogada(vez, matriz, jogador_x, jogador_o):
    while True:
        nome = jogador_x if vez == 'X' else jogador_o

        try:
            jogar = int(input(f'{nome} [{vez}], escolha uma posição (1-9): '))

            if jogar < 1 or jogar > 9:
                print('Digite um número de 1 a 9.')
                continue

        except ValueError:
            print('Digite uma posição válida.')
            continue

        except KeyboardInterrupt:
            print('\nSaindo...')
            exit()

        # Transforma posição em linha e coluna
        linha = (jogar - 1) // 3
        coluna = (jogar - 1) % 3

        # Verifica se a casa está livre
        if matriz[linha][coluna] in ('X', 'O'):
            print('Essa casa já está ocupada! Tente outra.')
            continue

        matriz[linha][coluna] = vez
        break


def verificar_vitoria(matriz, vez):
    # Linhas
    for i in range(3):
        if matriz[i][0] == vez and matriz[i][1] == vez and matriz[i][2] == vez:
            return True

    # Colunas
    for i in range(3):
        if matriz[0][i] == vez and matriz[1][i] == vez and matriz[2][i] == vez:
            return True

    # Diagonais
    if matriz[0][0] == vez and matriz[1][1] == vez and matriz[2][2] == vez:
        return True

    if matriz[0][2] == vez and matriz[1][1] == vez and matriz[2][0] == vez:
        return True

    return False


# Cadastro dos jogadores
jogador_x = input('Nome do jogador que será X: ').strip()
jogador_o = input('Nome do jogador que será O: ').strip()

if jogador_x == '':
    jogador_x = 'Jogador 1'

if jogador_o == '':
    jogador_o = 'Jogador 2'

# Tabuleiro
matriz = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7", "8", "9"]]

vez = 'X'

limpa_tela()

print(f'{jogador_x} jogará com [X]')
print(f'{jogador_o} jogará com [O]')
input('\nPressione Enter para começar...')

for rodada in range(9):
    limpa_tela()
    jogo(matriz)
    print()

    jogada(vez, matriz, jogador_x, jogador_o)

    if verificar_vitoria(matriz, vez):
        limpa_tela()
        jogo(matriz)

        vencedor = jogador_x if vez == 'X' else jogador_o
        print(f'\n🎉 PARABÉNS, {vencedor}! Você venceu jogando com [{vez}]!')
        break

    # Troca a vez
    if vez == 'X':
        vez = 'O'
    else:
        vez = 'X'

else:
    limpa_tela()
    jogo(matriz)
    print('\n🤝 Deu velha!')

print('\nFIM DE JOGO!')
