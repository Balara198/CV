import pygame
import pygame.gfxdraw

def benne(x, y, xmin, xmax, ymin, ymax):
    return x in range(xmin, xmax) and y in range(ymin, ymax)

def megnyit(nev, window):
    while True:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if nev == 'fomenu':
                if benne(x, y, 100, 700, 100, 270):
                    kirajzol('palyamenu', window)
                    return 'palyamenu'
                elif  benne(x, y, 100, 700, 430, 600):
                    return 'KILEPES'
                
            elif nev == 'jatek_kepernyo':
                if benne(x, y, 25, 105, 580, 610):
                    kirajzol('jatekmenu', window)
                    return 'jatekmenu'
                elif benne(x, y, 25, 105, 620, 650):
                    return 'SZIMULACIO'
                elif benne(x, y, 25, 105, 660, 690):
                    return 'FORGAT'
                elif benne(x, y, 140, 639, 100, 599):
                    return ((x-141)//100, (y-101)//100)
                elif benne(x, y, 690, 790, 50, 649):
                    return (649-y)//100
                
            elif nev == 'jatekmenu':
                if benne(x, y, 100, 700, 70, 240):
                    kirajzol('fomenu', window)
                    return 'fomenu'
                elif benne(x, y, 100, 700, 260, 436):
                    kirajzol('jatek_kepernyo', window)
                    return 'FOLYTAT'
                elif benne(x, y, 100, 700, 460, 630):
                    return 'KILEPES'
                
            elif nev == 'palyamenu':
                if benne(x, y, 100, 590, 100, 700) and (y-100)%100 in range(10, 90):
                    kirajzol('jatek_kepernyo', window)
                    return 'palya{}'.format((y-100)//100 +1)
                elif benne(x, y, 710, 790, 650, 690):
                    kirajzol('fomenu', window)
                    return 'fomenu'
                
            elif nev == 'gyozelem' or 'vereseg':
                if benne(x, y, 100, 700, 260, 435):
                    kirajzol('fomenu', window)
                    return 'fomenu'
                elif benne(x, y, 100, 700, 460, 630):
                    return 'KILEPES'
        elif event.type == pygame.QUIT:
            return 'KILEPES'

    
def kirajzol(nev, window):
    window.blit(pygame.image.load('{}.png'.format(nev)), (0, 0))
    pygame.display.update()
        
