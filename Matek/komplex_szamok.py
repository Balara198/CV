class Komplex:
    def __init__(self, re=0, im=0):
        self.re = self.r = re
        self.im = self.i = im
    def __add__(self, rhs):
        if type(rhs) is int or type(rhs) is float:
            rhs = Komplex(rhs)
        re = self.r + rhs.r
        im = self.i + rhs.i
        return Komplex(re, im)
    def __sub__(self, rhs):
        if type(rhs) is int or type(rhs) is float:
            rhs = Komplex(rhs)
        re = self.r - rhs.r
        im = self.i - rhs.i
        return Komplex(re, im)
    def __mul__(self, rhs):
        if type(rhs) is int or type(rhs) is float:
            rhs = Komplex(rhs)
        tmp = Komplex()
        tmp.r = self.r * rhs.r - self.i * rhs.i
        tmp.i = self.r * rhs.i + self.i * rhs.r
        return tmp
    def __imul__(self, rhs):
        if type(rhs) is int or type(rhs) is float:
            rhs = Komplex(rhs)
        return self*rhs
    def __pow__(self, rhs):
        tmp = self
        if rhs == 0:
            return Komplex(1)
        for i in range(rhs-1):
            tmp *=self
        return tmp
    def __ipow__(self, rhs):
        return self**rhs
    def __str__(self):
        return (f"{self.r} {'+' if self.i>=0 else '-'} {abs(self.i)}i")

def mandel_e(c, depth=10):
    z = Komplex()
    for i in range(depth):
        z = z**2+c
        print(z)
def main():
    a = Komplex(0, 0.9)
    mandel_e(a, 1000)
main()
