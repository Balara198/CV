import random

szamok = []
lkkt = 2520
for i in range(1, 11):
    szamok += [i for j in range(int(lkkt/i))]
hossz = 7381
'''
for i in range(10):
    print('')
    for j in range(10):
        print(szamok[random.randint(0, 7380)], end=' ')
'''
for i in range(15):
    nev = bin(i)[2:]
    print('0'*(4-len(nev))+nev+'.png')