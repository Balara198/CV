def fakt(a):
    ret = 1
    for i in range(a):
        ret *= a-i
    return ret

def nCr(a, b):
    return int(fakt(a)/fakt(a-b)/fakt(b))

def pow(a,b,n):
    ret = 0
    for i in range(n+1):
        ret += nCr(n, i)*(a**i*b**(n-i))
    return ret

print(pow(1,1,10))
