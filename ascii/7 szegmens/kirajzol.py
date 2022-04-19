import os,time
from kiir import *

def cls(n = 0):
    if n == 0:
        os.system('cls')
    else:
        print('\b'*n)


szam = 17000
digit = len(str(szam))

for szam in range(szam):
    n = 0
    kep = dekodol(8, 5)
    time.sleep(0.00001)
    cls(n)
    n = len(kep)
    print(kep)

    