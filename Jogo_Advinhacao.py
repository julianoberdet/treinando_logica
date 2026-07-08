from random import randint

pc = randint(1,50)
tentativas = 0

while True:
    palpite = int(input('Digite um palpite de (1 a 50): '))
    tentativas += 1
    print('-' * 30)

    if palpite < pc:
        print('Mais... Tente novamente')
    elif palpite > pc:
        print('Menos... Tente novamente')
    elif palpite == pc:
        print(f'Isso! O computador pensou no número {pc}, e você acertou com {tentativas} tentativas')
        break