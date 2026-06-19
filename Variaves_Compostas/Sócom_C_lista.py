c = []
tot = 0
for i in range(0,5):
    nome = str(input('Digite seu nome: ')).strip()
    if nome.upper()[0] == 'C':
        tot += 1
        c.append(nome)
print('-' * 35)
print('LISTAGEM FINAL'.center(35))
print('-'*35)
print(f'Foram {tot} nomes que começam com C')
print('Os nomes são:')
for i in c:
    print(f'{i}')
print('-' * 35)
