import pygame
import pygame.gfxdraw

def inverz(a):
    r = 255-int(a[0])
    g = 255-int(a[1])
    b = 255-int(a[2])
    return pygame.Color(r, g, b)

def fkfh(a):
    r = int(a[0])
    g = int(a[1])
    b = int(a[2])
    sz = int((r+g+b)/3)
    return pygame.Color(sz, sz, sz)

def atlag(a, c):
    r = int((a[0]+c[0])/2)
    g = int((a[1]+c[1])/2)
    b = int((a[2]+c[2])/2)
    return pygame.Color(r, g, b)

def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('színek szorzása')

    kep1 = pygame.image.load('kep1.png')
    kep2 = pygame.image.load('kep2.png')

    window.blit(kep1, (0, 0))
    window.blit(kep2, (500, 0))
    window.blit(kep1, (0, 500))
    pygame.display.update()

    
    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y))[:3]
            szin2 = window.get_at((x+500, y))[:3]
            pygame.gfxdraw.pixel(window, x, y, atlag(szin1, szin2))
            pygame.gfxdraw.pixel(window, x+500, y+500, fkfh(szin1))
        pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y+500))[:3]
            szin2 = window.get_at((x+500, y+500))[:3]
            pygame.gfxdraw.pixel(window, x+500, y, atlag(szin1, szin2))
        pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin = window.get_at((x, y+500))[:3]
            pygame.gfxdraw.pixel(window, x, y, inverz(szin))
        pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y))[:3]
            szin2 = window.get_at((x+500, y))[:3]
            pygame.gfxdraw.pixel(window, x+500, y, atlag(szin1, (100, 155, 50)))
            
    for y in range(500):
        for x in range(500):
            szin1 = window.get_at((x, y))[:3]
            szin2 = window.get_at((x+500, y))[:3]
            pygame.gfxdraw.pixel(window, x+500, y, atlag(szin1, szin2))
            pygame.gfxdraw.pixel(window, x+500, y+500, inverz(szin2))           
        pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y+500))[:3]
            szin2 = window.get_at((x+500, y+500))[:3]
            pygame.gfxdraw.pixel(window, y+500, x, atlag(szin1, szin2))           
            if y%50 == 0:
                pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin = window.get_at((x, y))[:3]
            pygame.gfxdraw.pixel(window, y+500, x, inverz(szin))        
        pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y))[:3]
            szin2 = window.get_at((x+500, y))[:3]
            pygame.gfxdraw.pixel(window, x+500, y, atlag(szin1, szin2))
        pygame.display.update()

    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y+500))[:3]
            szin2 = window.get_at((x+500, y))[:3]
            szin3 = window.get_at((x+500, y+500))[:3]
            pygame.gfxdraw.pixel(window, x, y, atlag(szin1, szin2))
            pygame.gfxdraw.pixel(window, x+500, y, atlag(szin1, szin3))
        pygame.display.update()
main()


            
