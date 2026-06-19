lista = []
maior =  menor = 0


for c in range(0,5):
    lista.append(int(input('Digite um número: ')))
    if c == 1:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]


print('A lista ficou assim',end='')
for c in lista:
    print(f' -> {c}',end='')
print()


print(f'O maior número digitado foi {maior} nas posições: ',end='')
for i , v in enumerate(lista):
    if v == maior:
        print(f'{i+1}..',end='')
print()


print(f'O menor número digitado foi {menor} nas posições: ',end='')
for v, i in enumerate(lista):
    if i == menor:
        print(f'{v+1}..',end='')