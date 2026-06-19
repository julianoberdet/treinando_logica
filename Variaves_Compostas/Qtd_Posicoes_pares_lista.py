v = []
par = 0
for c in range(0,7):
    n = int(input(f'Digite o {c+1}º numero: '))
    v.append(n)
print('-'*35)
for i,j in enumerate(v):
    if j % 2 == 0:
        par += 1
        print(f'Valor par na posição {i+1} e o valor foi {j}')
print(f'Foram digitados {par} valores pares')