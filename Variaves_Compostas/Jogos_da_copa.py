from random import randint, shuffle

# -----------------------------
# GRUPOS
# -----------------------------
grupos = [
    ['México','Africa do Sul','Coreia do Sul','Republica Tcheca'],
    ['Canadá','Bosnia','Catar','Suiça'],
    ['Brasil','Marrocos','Haiti','Escocia'],
    ['Estados Unidos','Paraguai','Austrália','Turquia'],
    ['Alemanha','Curaçau','Costa do Marfim','Equador'],
    ['Holanda','Japão','Suécia','Tunisia'],
    ['Bélgica','Egito','Irã','Nova Zelândia'],
    ['Espanha','Cabo Verde','Arabia Saudita','Uruguai'],
    ['França','Senegal','Iraque','Noruega'],
    ['Austria','Jordânia','Argentina','Argélia'],
    ['Portugal','RD do Congo','Uzbequistão','Colômbia'],
    ['Inglaterra','Croácia','Gana','Panamá']
]

jogos_grupo = [
    (0,1),(2,3),
    (0,2),(3,1),
    (3,0),(1,2)
]

primeiros = []
segundos = []
terceiros_dados = []

# -----------------------------
# FASE DE GRUPOS
# -----------------------------
for n, grupo in enumerate(grupos, start=1):
    print(f'\n=== GRUPO {n} ===')

    tabela = {}

    for time in grupo:
        tabela[time] = {'pts':0,'gp':0,'gc':0,'sg':0}

    for i, j in jogos_grupo:
        t1, t2 = grupo[i], grupo[j]

        g1, g2 = randint(0,5), randint(0,5)

        print(f'{t1} {g1} x {g2} {t2}')

        tabela[t1]['gp'] += g1
        tabela[t1]['gc'] += g2
        tabela[t2]['gp'] += g2
        tabela[t2]['gc'] += g1

        if g1 > g2:
            tabela[t1]['pts'] += 3
        elif g2 > g1:
            tabela[t2]['pts'] += 3
        else:
            tabela[t1]['pts'] += 1
            tabela[t2]['pts'] += 1

    for t in tabela:
        tabela[t]['sg'] = tabela[t]['gp'] - tabela[t]['gc']

    classificados = sorted(
        tabela.items(),
        key=lambda x: (x[1]['pts'], x[1]['sg'], x[1]['gp']),
        reverse=True
    )

    print('\nClassificação:')
    for pos, (time, dados) in enumerate(classificados, start=1):
        print(f'{pos}º {time} - {dados["pts"]} pts')

    # guardar classificados
    primeiros.append(classificados[0][0])
    segundos.append(classificados[1][0])
    terceiros_dados.append(classificados[2])

# -----------------------------
# MELHORES 3º COLOCADOS
# -----------------------------
melhores_terceiros = sorted(
    terceiros_dados,
    key=lambda x: (x[1]['pts'], x[1]['sg'], x[1]['gp']),
    reverse=True
)[:8]

# -----------------------------
# FASE DE 32 (ROUND OF 32)
# -----------------------------
fase_32 = primeiros + segundos + [t[0] for t in melhores_terceiros]

shuffle(fase_32)

print('\n\n=== FASE DE 32 ===')

def jogo_mata(t1, t2):
    g1, g2 = randint(0,5), randint(0,5)

    while g1 == g2:
        g1 += randint(0,1)
        g2 += randint(0,1)

    vencedor = t1 if g1 > g2 else t2
    print(f'{t1} {g1} x {g2} {t2} -> {vencedor}')
    return vencedor

# -----------------------------
# OITAVAS EM DIANTE
# -----------------------------
def fase_mata(lista):
    vencedores = []

    for i in range(0, len(lista), 2):
        vencedores.append(jogo_mata(lista[i], lista[i+1]))

    return vencedores


# 32 -> 16
oitavas = fase_mata(fase_32)
print('\n=== OITAVAS DE FINAL ===')
# 16 -> 8
quartas = fase_mata(oitavas)
print('\n=== QUARTAS DE FINAL ===')
# 8 -> 4
semis = fase_mata(quartas)
print('\n=== SEMI FINAL ===')
# 4 -> 2
final = fase_mata(semis)

# FINAL
print('\n=== FINAL ===')
campeao = jogo_mata(final[0], final[1])

print(f'\n🏆 CAMPEÃO: {campeao}')