gabarito = []
alunos = []
resposta = []

def cadastrogabarito():
    print('CADASTRO DE GABARITO'.center(40))
    print('-' * 40)
    for c in range(5):
        gab = str(input(f'QUESTÃO {c+1}: ')).upper()
        gabarito.append(gab)


def cadastroprova():
    nota = 0
    print('RESPOSTAS DADAS')
    for j in range(5):
        resposta_aluno = ' '
        while resposta_aluno not in ['A','B','C','D','E']:
            resposta_aluno = str(input(f'QUESTÃO {j+1}: ')).strip().upper()
        if resposta_aluno == gabarito[j]:
            nota += 2
    return nota


cadastrogabarito()
for i in range(3):
    print('-' * 40)
    print(f'ALUNO {i+1}'.center(40))
    print('-' * 40)

    alunos.append(str(input('Nome: ')))
    resposta.append(cadastroprova())


#Notas finais
print('-' * 40)
print('NOTAS FINAIS'.center(40))
print('-' * 40)
for c in range(len(alunos)):
    print(f'{alunos[c]} - {resposta[c]}')
media = sum(resposta) / len(resposta)
print('-' * 40)
print(f'A média da turma foi {media:.2f}')