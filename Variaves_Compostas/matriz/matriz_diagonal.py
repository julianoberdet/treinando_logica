matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        if l == c:
            matriz[l][c] = 1
        else:
            matriz[l][c] = 0

print('=' * 30)
print('MATRIZ IDENTIDADE 3ª ORDEM'.center(30))
print('=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f' [{matriz[l][c]:^5}] ',end='')
    print()