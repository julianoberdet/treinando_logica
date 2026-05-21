from time import sleep
C = 1
while True:
    print(C)
    C += 1
    sleep(1)
    if C > 10:
        break
