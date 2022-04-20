import pygame
import pygame.gfxdraw

def kever(a, b):
    t = 3
    r = a[0] if a[0]<b[0] else int((b[0]+a[0])/t)
    g = a[1] if a[1]<b[1] else int((b[1]+a[1])/t)
    b = a[2] if a[2]<b[2] else int((b[2]+a[2])/t)
    return pygame.Color(r,g,b)

def main():
    pygame.init()
    window = pygame.display.set_mode((360, 280))
    pygame.display.set_caption('japflag')

    kep1 = pygame.image.load('jap.png')
    kep2 = pygame.image.load('sz.png')
    window.blit(kep1, (0, 0))
    window.blit(kep2, (180, 0))

    for x in range(180):
        for y in range(280):
            szin = window.get_at((x, y))[:3]
            szin2 = window.get_at((x+180, y))[:3]
            if szin[0] in range(120, 190) and szin[1] in range(120, 190):
                pygame.gfxdraw.pixel(window, x, y, kever(szin, szin2))
        pygame.display.update()

main()
