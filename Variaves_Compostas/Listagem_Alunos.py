#Variaveis Compostas
aluno = []
n1 = []
n2 = []
media = []
#Variaveis Simples
SM = MT = Tot = 0


#Captar dados
for c in range(4):
    print('=' * 30)
    print(f'ALUNO {c+1}'.center(30))
    print('='*30)
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    m = (nota1 + nota2) / 2


    # Colocar nas listas
    aluno.append(nome)
    n1.append(nota1)
    n2.append(nota2)
    media.append(m)

    #Soma das médias dos alunos
    SM += m

#Media da turma
MT = SM / 4

# Mostrar o Resultado
print()
print('LISTAGEM DE ALUNOS'.center(30))
print('='*30)
for c in range(4):
    print(f'{aluno[c]:<20}{media[c]}')
    if media[c] > MT:
        Tot += 1

print('='*30)
print()
print(f'Ao todo temos {Tot} alunos acima da média da turma que foi {MT:.2f}')
print()
print('='*30)
print("Alunos acima da média da turma:")
print('='*30)
for c in range(4):
    if media[c] > MT:
        print(f"- {aluno[c]} ({media[c]:.1f})")
print('='*30)