from BLOKK import Blokk

def betolt(nev):
    jatekter = [[], [], [], [], []]
    eszkoztar = []
    start = None
    with open('{}.txt'.format(nev), 'rt') as palya:
        sor = palya.readline().rstrip('\n')
        x = 0
        y = 0
        for i in range(len(sor)):
            elem = sor[i]
            if elem == 'u':
                jatekter[y].append(Blokk('ures', 0))
                
            elif elem == 'v':
                jatekter[y].append(Blokk('stop', 0))
                
            elif elem == 'b':
                jatekter[y].append(Blokk('akadaly', 0))
            
            elif elem == 's':
                jatekter[y].append(Blokk('start', int(sor[i+1])))
                start = (x, y)

            if elem == ' ':
                y += 1
                x = 0
                        
            elif elem not in ['0','1','2','3']:
                x += 1
                
        sor = palya.readline().rstrip('\n')
        for elem in sor:
            if elem == "t":
                eszkoztar.append(Blokk('tukor', 0))
            else:
                eszkoztar.append(Blokk('f_tukor', 0))

    return jatekter, eszkoztar, start
