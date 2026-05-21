n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = n + (10-1) * r
for c in range(n, termo+r, r):
    print(c,end=' -> ')
print('ACABOU')