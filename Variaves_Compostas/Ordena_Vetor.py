vet = [0] * 4

# Leitura dos valores
for i in range(4):
    vet[i] = int(input("Digite um valor: "))

# Ordenação
for i in range(3):
    for j in range(i + 1, 4):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

# Exibição
for i in range(4):
    print(f"{{{vet[i]}}}", end="")



#VERSÃO PYTHONICA
'''vet = []

for i in range(4):
    vet.append(int(input('Digite um valor: ')))

vet.sort()

for valor in vet:
    print(f"{{{valor}}}", end="")'''
