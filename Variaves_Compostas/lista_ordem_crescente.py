lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, Tente outro!')


    #Pergunta se o usuário quer continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

#Ordena a lista em ordem crescente
lista.sort()
print(f'A lista em ordem crescente ficou assim {lista}')