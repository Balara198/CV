import time, os, random

def display(chars):
    s = '\n'.join(''.join(row) for row in chars)
    print(s)
    return len(s)
    
def cls(n = 0):
    if n == 0:
        os.system('cls')
    else:
        print('\b'*n)

chars = []
for i in range(40):
    chars.append(["-"]*40)

for i in range(100):
    n = 0
    r = random.randint(0,39)
    c = random.randint(0,39)
    chars[r][c] = "X"
    time.sleep(0.1)
    cls(n)
    n = display(chars)