primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da Pa: '))
termo = primeiro
c = 0
usuario = 10
total = 0
while usuario != 0:
    total += usuario
    while c < total:
        print(f'{termo} -> ',end='')
        termo += razao
        c += 1
    print('PAUSA')
    usuario = int(input('Quantos termos mais você quer? '))
print(f'Ao final da progressão foram {total} termos')



