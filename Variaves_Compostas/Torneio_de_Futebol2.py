# Jogos de ida e volta com pontuação
from random import randint

def cabecalho(txt):
    print('=' * 40)
    print(txt.center(40))
    print('=' * 40)

# Cadastro dos times
cabecalho('TORNEIO DE FUTEBOL')

times = []

for c in range(4):
    nome = input(f'Escolha o {c+1}º time: ').strip()
    times.append({
        'nome': nome,
        'v': 0,
        'e': 0,
        'd': 0,
        'gp': 0,
        'gc': 0,
        'pts': 0
    })

# Jogos
cabecalho('TABELA DE JOGOS')

for c in range(len(times)):
    for j in range(c + 1, len(times)):

        # IDA
        casa = randint(0, 5)
        fora = randint(0, 5)

        print(f'{times[c]["nome"]} {casa} x {fora} {times[j]["nome"]}'.center(40))

        times[c]['gp'] += casa
        times[c]['gc'] += fora
        times[j]['gp'] += fora
        times[j]['gc'] += casa

        if casa > fora:
            times[c]['v'] += 1
            times[c]['pts'] += 3
            times[j]['d'] += 1

        elif fora > casa:
            times[j]['v'] += 1
            times[j]['pts'] += 3
            times[c]['d'] += 1

        else:
            times[c]['e'] += 1
            times[j]['e'] += 1
            times[c]['pts'] += 1
            times[j]['pts'] += 1

        # VOLTA
        casa = randint(0, 5)
        fora = randint(0, 5)

        print(f'{times[j]["nome"]} {casa} x {fora} {times[c]["nome"]}'.center(40))

        times[j]['gp'] += casa
        times[j]['gc'] += fora
        times[c]['gp'] += fora
        times[c]['gc'] += casa

        if casa > fora:
            times[j]['v'] += 1
            times[j]['pts'] += 3
            times[c]['d'] += 1

        elif fora > casa:
            times[c]['v'] += 1
            times[c]['pts'] += 3
            times[j]['d'] += 1

        else:
            times[c]['e'] += 1
            times[j]['e'] += 1
            times[c]['pts'] += 1
            times[j]['pts'] += 1

# Classificação
cabecalho('CLASSIFICAÇÃO')

times.sort(
    key=lambda x: (x['pts'], x['gp'] - x['gc'], x['gp']),
    reverse=True
)

print(f'{"TIME":15} {"V":>3} {"E":>3} {"D":>3} {"GP":>4} {"GC":>4} {"SG":>4} {"PTS":>5}')

for t in times:
    sg = t['gp'] - t['gc']
    print(f'{t["nome"]:15} {t["v"]:>3} {t["e"]:>3} {t["d"]:>3} {t["gp"]:>4} {t["gc"]:>4} {sg:>4} {t["pts"]:>5}')

print(f'\nCampeão: {times[0]["nome"]}')