def dekodol(szam, digit):

    #Számjegyekhez tartozó szegmensek
    szamjegyek = [[1,1,1,1,1,1,0],
              [0,1,1,0,0,0,0],
              [1,1,0,1,1,0,1],
              [1,1,1,1,0,0,1],
              [0,1,1,0,0,1,1],
              [1,0,1,1,0,1,1],
              [1,0,1,1,1,1,1],
              [1,1,1,0,0,0,0],
              [1,1,1,1,1,1,1],
              [1,1,1,1,0,1,1]]
    
    #a szegmenseket alkotó karakterek pozíciója egy 14*11-karakteres területen
    szegmensek = [[(1,4),(1,5),(1,6),(1,7),(1,8),(1,9)],
                  [(2,10),(2,11),(3,10),(3,11),(4,10),(4,11)],
                  [(6,10),(6,11),(7,10),(7,11),(8,10),(8,11)],
                  [(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)],
                  [(6,2),(6,3),(7,2),(7,3),(8,2),(8,3)],
                  [(2,2),(2,3),(3,2),(3,3),(4,2),(4,3)],
                  [(5,4),(5,5),(5,6),(5,7),(5,8),(5,9)]]
    
    #a megjelenítendő szám helyiértékekre bontott sztringje
    szam = str(szam)
    if len(szam) != digit:
        szam = '0'*(digit-len(szam)) + szam
    szam = list(szam)
    
    cm = [(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
          (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
          (0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0),
          (0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0),
          (0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0),
          (0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0),
          (0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0),
          (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)]
    
    #a megjelenítési terület, ahágy helyiérték, 
    #sorban annyi 14*11-karakteres téglalap alkotja.
    sorok = []
    #blank = '▒'*(14*digit) 
    blank = '|'*(14*digit) 
    for i in range(11):
        tmp = ''
        for k in cm[i]:
            if k: 
                tmp+= '█'
            else:
                tmp+= '|'
        hhh = blank+tmp
        sorok.append(hhh)
    
    #A megjelenítési terület sorai listában tároltak,
    #de a sorok elemeit is listába kell rendezni, hogy
    #azok értékeit egyesével lehessen módosítani.
    for i in range(len(sorok)):
        sorok[i] = list(sorok[i])
    
    #A h ciklus annyiszor fut le, ahány helyiértéke van az adott
    #számnak.
    for h in range(len(szam)):
        #Az adott helyiérték visszaalakítás integerré.
        szamjegy = int(szam[h])
        #az első átmeneti változó tartalmazza a hétszegmenses
        #dekódolótáblázat megfelelő számjegyhez tartozó sorát.
        temp = szamjegyek[szamjegy]
        #Az i ciklus vizsgálja a szegmensek igazságtartalmát.
        for i in range(len(temp)):
            if temp[i]:
            #a második átmeneti változó tartalmazza a megfelelő
            #szegmens pozícióját egy helyiértéknyi területen.
                temp2 = szegmensek[i]
                for j in range(len(temp2)):
                #az karakter pozíciójának meghatározása az egy helyiértéknyi
                #pozíciója plusz a helyiértéknyi eltolás.
                    sor = temp2[j][0] 
                    oszlop = temp2[j][1] + 14*(h)
                    #sorok[sor][oszlop] = '█'
                    sorok[sor][oszlop] = '█'

    for i in range(len(sorok)):
        sorok[i].append('\n')
        sorok[i] = "".join(sorok[i])
        
    sorok = "".join(sorok)
    return sorok
