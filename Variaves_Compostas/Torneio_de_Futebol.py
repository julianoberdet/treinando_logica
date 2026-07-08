def cabecalho(txt):
    print('=' * 40)
    print(txt.center(40))
    print('=' * 40)


times = []
cabecalho('TORNEIO DE FUTEBOL')
for c in range(4):
    times.append(str(input(f'Digite o {c+1}º time: ')).strip())

cabecalho('TABELA DE JOGOS')
for c in range(len(times)):
    for i in range(len(times)):
        if c != i:
            print(f'{times[c]} X {times[i]}'.center(40))

print('=' * 40)
