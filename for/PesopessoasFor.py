maior = menor = 0
for c in range(1,6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}kg')
print(f'O menor peso foi {menor}kg')

