from datetime import date
maior = menor = idade = 0
atual = date.today().year
for p in range(1,8):
    nasc = int(input(f'Data de nascimento da {p}ª pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'No total são {maior} \033[32mMAIORES\033[m de 21 anos')
print(f'No total são {menor} \033[31mMENORES\033[m de 21 anos')

