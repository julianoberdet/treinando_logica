def fibonacci(n1,n2,v):
    c = 2
    if v <= 1:
        print(f'{n1} -> ', end='')
    else:
        print(f'{n1} -> {n2} -> ', end='')
    while c < v:
        if v > 1:
                n3 = n1 + n2
                print(f'{n3} -> ',end='')
                n1 = n2
                n2 = n3
        c += 1
    print('FIM')
    return v


n = int(input('Quantos termos você quer? '))
t1 = 0
t2 = 1
f = fibonacci(t1,t2,n)