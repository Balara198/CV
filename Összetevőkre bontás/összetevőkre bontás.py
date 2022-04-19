def lag(i, n):
    sor = f"L{i}="
    sorveg = ""
    for j in range(1, n+1):
        if j==i:
            continue
        else:
            sor += f"(A-la({j})*E)*"
            sorveg += f"/(la({i})-la({j}))"
    sor = sor[:-1]
    sor += sorveg+";"
    return sor
def main():
    meret = int(input("Az A mátrix mérete: "))
    A = []
    B = []
    C = []
    D = 0
    sor = ''
    temp = None
    for i in range(meret):
        temp = []
        for j in range(meret):
            elem = float(input(f"A{i+1}{j+1}: "))
            temp.append(elem) if int(elem) != float(elem) else temp.append(int(elem))
        A.append(temp)
    for i in range(meret):
        elem = float(input(f"B{i+1}: "))
        B.append(elem) if int(elem) != float(elem) else B.append(int(elem))
    for i in range(meret):
        elem = float(input(f"C{i+1}: "))
        C.append(elem) if int(elem) != float(elem) else C.append(int(elem))
    D = float(input("D: "))
    D = D if float(D) != int(D) else int(D)
    imp = int(input("impulzusválasz v. ugrásválasz (1/0):"))
    print()
    
    sor += "A=["
    for i in A:
        for j in i:
            sor+=f"{j} "
        sor=sor[:-1]
        sor+=";"
    sor = sor[:-1]
    sor += "]; B=["
    for i in B:
        sor += f"{i};"
    sor = sor[:-1]
    sor+="]; C=["
    for i in C:
        sor+=f"{i} "
    sor = sor[:-1]
    sor+=f"]; D={D};"
    print(sor)
    
    print("la=eig(A);")
    
    print(f"E=eye({meret})")
    
    for i in range(meret):
        print(lag(i+1, meret))
        
    for i in range(1, meret+1):
        print(f"K{i}=C*L{i}*B;")
        
    print(f"t3=round(-5/min(la))")
    
    print(f"t=-0.1:0.01:t3;")
    
    if imp:
        sor="h=stepfun(t,0).*("
        for i in range(1, meret+1):
            sor+=f"K{i}.*exp(la({i}).*t)+"
        sor = sor[:-1]
        sor += ");"
        print(sor)
        print("plot(t,h)")
        
    else:
        sor=f"al={D}"
        sor2="g=stepfun(t,0).*(al"
        for i in range(1, meret+1):
            sor+=f"-K{i}/la({i})"
            sor2+=f"+(K{i}/la({i})).*exp(la({i}).*t)"
        sor+=";"
        print(sor)
        
        sor2+=");"
        print(sor2)
        
        print("plot(t,g)")
    #legkisebb sajátérték reciprokának mínusz ötszöröse
main()