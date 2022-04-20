import pygame
import pygame.gfxdraw

def atlag(a, c):
    r = int((a[0]+c[0])/2)
    g = int((a[1]+c[1])/2)
    b = int((a[2]+c[2])/2)
    return pygame.Color(r, g, b)

def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('reklam')

    kep = pygame.image.load('kep1.png')

    window.blit(kep, (0, 0))
    window.blit(kep, (500, 0))
    window.blit(kep, (0, 500))
    window.blit(kep, (500, 500))

    b = (0, 0, 255)
    c = (0, 127, 128)
    g = (0, 255, 0)
    p = (128, 0, 128)
    y = (128, 128, 0)
    r = (255, 0, 0)

    szinek = [r, c, y, g, p, b]

    for x in range(500):
        for y in range(500):
            szin1 = window.get_at((x, y))[:3]
            szin2 = b
            pygame.gfxdraw.pixel(window, x, y, atlag(szin1, szin2))
    pygame.display.update()

    szin = 0
    negy = 0
    for i in range(100):
        szin = ((i%6))//1
        if negy > 4:
            negy = 1
        else:
            negy += 1

        print(negy, end=", ")
        print(szin)
        
        for x in range(500):
            for y in range(500):
                szin1 = window.get_at((x+500, y))[:3]
                szin2 = szinek[szin]
                pygame.gfxdraw.pixel(window, x, y, atlag(szin1, szin2))
            pygame.display.update()

        szin = ((szin+1)%6)//1
        for y in range(500):
            for x in range(500):
                szin1 = window.get_at((x+500, y+500))[:3]
                szin2 = szinek[szin]
                pygame.gfxdraw.pixel(window, x+500, y, atlag(szin1, szin2))
            pygame.display.update()

        szin = ((szin+1)%6)//1
        for x in range(500, 0, -1):
            for y in range(500):
                szin1 = window.get_at((x, y+500))[:3]
                szin2 = szinek[szin]
                pygame.gfxdraw.pixel(window, x+500, y+500, atlag(szin1, szin2))
            pygame.display.update()

        szin = ((szin+1)%6)//1
        for y in range(500, 0, -1):
            for x in range(500, 0, -1):
                szin1 = window.get_at((x, y))[:3]
                szin2 = szinek[szin]
                pygame.gfxdraw.pixel(window, x, y+500, atlag(szin1, szin2))
            pygame.display.update()


main()
