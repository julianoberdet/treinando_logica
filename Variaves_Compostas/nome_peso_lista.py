temp = []
princ= []
mai = men = 0
def cabecalho(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


cabecalho('LISTA DE PESSOAS')
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    #Saber o maior e menor peso
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    #Se o usuario quer ou não continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('-' * 40)

cabecalho('ESTATISTICA FINAL')
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O menor peso foi {men}kg peso de',end='')
for p in princ:
    if p[1] == men:
        print(f' [{p[0]}]' ,end='')
print()

print(f'O maior peso foi {mai}kg peso de',end='')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}] ',end='')
print()