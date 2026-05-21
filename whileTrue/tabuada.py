while True:
    n = int(input('Qual número quer saber a tabuada: '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-' *40)
print('PROGRAMA DE TABUADA ENCERRADO! volte sempre!')