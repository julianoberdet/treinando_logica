gabarito = []
alunos = []
prova = []
notas = []

print('PASSO 1 - CADASTRO DE GABARITO')
print('-' * 40)
for c in range(5):
    gab = str(input(f'QUESTÃO {c+1}: ')).upper()
    gabarito.append(gab)

for c in range(3):
    print('-' * 40)
    print(f'ALUNO {c+1}'.center(40))
    print('-' * 40)
    alunos.append(str(input('NOME: ')))

    resposta = []
    print('RESPOSTAS DADAS')
    for i in range(1,6):
        q = ' '
        while q not in 'ABCDE':
            q = (str(input(f'QUESTÃO {i}: '))).strip().upper()
        resposta.append(q)

    prova.append(resposta[:])
for i in range(len(alunos)):
    nota = 0
    for j in range(5):
        if gabarito[j] == prova[i][j]:
            nota += 2
    notas.append(nota)

print('NOTAS FINAIS'.center(40))
print('-' * 40)
for v in range(len(alunos)):
    print(f'{alunos[v]} - {notas[v]}')
media = sum(notas) / len(alunos)
print('-' * 40)
print(f'Média da turma {media:.2f}')



'''gabarito = []
aluno = []
prova = []
notas = []

print('PASSO 1 - CADASTRO DE GABARITO')
print('-' * 40)
for c in range(5):
    gab = ' '
    while gab not in ['A','B','C','D','E']:
        gab = str(input(f'QUESTÃO {c+1}: ')).strip().upper()
    gabarito.append(gab)

for a in range(3):
    print('-'*40)
    print(f'ALUNO {a+1}'.center(40))
    print('-'*40)
    aluno.append(str(input('Nome: ')))
    print('RESPOSTAS DADAS')
    respostas = []
    for c in range(5):
        resp = ' '
        while resp not in ['A','B','C','D','E']:
            resp = str(input(f'QUESTÃO {c+1}: ')).strip().upper()
        respostas.append(resp)
    prova.append(respostas[:])
    pts = 0
    for q in range(5):
        if gabarito[q] == prova[a][q]:
            pts += 2
    notas.append(pts)
    
    
print('-' * 40)
print('NOTAS FINAIS'.center(40))
print('-' * 40)
for c in range(len(aluno)):
    print(f'{aluno[c]}  -  {notas[c]}'.center(40))
media = sum(notas) / len(notas)
print('-' * 40)
print(f'A média da turma foi {media:.2f}')'''