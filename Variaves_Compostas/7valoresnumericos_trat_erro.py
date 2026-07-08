numeros = [[],[]]
for c in range(7):
    while True:
        try:
            n = int(input(f'Digite o {c+1}º valor: '))
            break
        except ValueError:
            print('ERRO com os dados digitados')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            exit()
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'Os números pares em ordem crescente {sorted(numeros[0])}')
print(f'Os números impares em ordem crescente {sorted(numeros[1])}')