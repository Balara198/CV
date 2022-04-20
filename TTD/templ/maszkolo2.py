import pygame, random
import pygame.gfxdraw

def arnyal(szin, mertek):
    r = szin[0]-mertek
    g = szin[1]-mertek
    b = szin[2]-mertek
    r = 0 if r<0 else r
    g = 0 if g<0 else g
    b = 0 if b<0 else b
    r = 255 if r>255 else r
    g = 255 if g>255 else g
    b = 255 if b>255 else b
    return pygame.Color(r,g,b)
    
    

def zajoz(szoras, window):
    for x in range(64):
        for y in range(40):
            szin = window.get_at((x, y))[:3]
            if szin[0] == 237:
                szin = pygame.Color(15, 67, 43)
                mertek = [1, -1][random.randint(0,1)]*szoras[random.randint(0, 7380)]
                szin = arnyal(szin, mertek)
            elif szin[1] != 0 and szin[0] < szin[1]:
                mertek = [1, -1][random.randint(0,1)]*szoras[random.randint(0, 7380)]
                szin = arnyal(szin, 3*mertek)
            pygame.gfxdraw.pixel(window, x, y, szin)
            

def main():
    pygame.init()
    window = pygame.display.set_mode((64, 40))
    pygame.display.set_caption('zajosítás')
    
    szoras = []
    lkkt = 2520
    for i in range(1, 11):
        szoras += [i for j in range(int(lkkt/i))]
        
    for i in range(15):
        nev = bin(i)[2:]
        f = '0'*(4-len(nev))+nev+'.png'
    
        kep = pygame.image.load(f)
        ujFajlNev = 'uj'+f
        window.blit(kep, (0, 0))
    
        zajoz(szoras, window)
        ujKep = pygame.Surface((64, 40))
        ujKep.blit(window, (0,0), pygame.Rect((0,0), (64, 40)))
        pygame.image.save(ujKep, ujFajlNev)
        
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()

main()
