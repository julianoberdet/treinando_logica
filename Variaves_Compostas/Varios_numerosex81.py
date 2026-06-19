numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))


    #Pergunta pro usuario se quer continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break


print(f'Foram digitados {len(numeros)} números')

#Ordem crescente
print()
numeros.sort()
print('Os números em ordem crescente',end='')
for c in numeros:
    print(f' -> {c}',end='')

#Ordem decrescente
print()
numeros.sort(reverse=True)
print('Os números em ordem decrescente',end='')
for c in numeros:
    print(f' -> {c}',end='')

#Verifica se tem o número 5 na lista
print()
if 5 in numeros:
    print('O número 5 \033[32mFOI\033[m digitado')
else:
    print('O número 5 \033[31mNÃO FOI\033[m digitado')