C = 1
TotN = 0
while True:
    N = int(input("Digite um número: "))
    C += 1
    if N < 0:
        TotN += 1
    if C > 5:
        break
print(f'Foram digitados {TotN} números negativos')