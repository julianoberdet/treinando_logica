total = mais1000 = menor = c = 0
mais_barato = ''
print('='*40)
print('\033[32;1m         LOJA MELHOR PREÇO\033[m'.center(40))
print('='*40)

#Capitação de dados
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto:R$ '))
    print('='*40)
    total += preco #Para ver o total da compra
    c += 1

#Condicionais para ver resultados dos dados
    if preco > 1000:
        mais1000 += 1
    if c == 1:
        menor = preco
        mais_barato = nome
    else:
        if preco < menor:
            menor = preco
            mais_barato = nome

#Pergunta se quer ou não continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        print('-'*40)
    if resp in 'N':
        break

#Resultado final
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'Foram {mais1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {mais_barato} custando R${menor:.2f}')
