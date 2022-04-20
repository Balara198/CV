a = int(input('oldalhossz: '))

sor1 = ""
sor2 = ""

for i in range(4):
    sor1 += "X"*a + "."*a
    sor2 += "."*a + "X"*a

sor1 += '\n'
sor2 += '\n'
sor1 *= a
sor2 *= a

sor = (sor1+sor2) * 4
print(sor)
