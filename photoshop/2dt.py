import pygame
import pygame.gfxdraw
import math

def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('2d')

    d = 10
    s = 0
    a = s
    b = a+d
    
    for t in range(500):
        for x in range(500):
            if a<x-250<b:
                pygame.gfxdraw.pixel(window, x, 499-t, (0, 0, 255))
            elif 500-a>x+250>500-b:
                pygame.gfxdraw.pixel(window, x, 499-t, (0, 255, 0))
            else:
                pygame.gfxdraw.pixel(window, x, 499-t, (255, 0, 0))
        s+=1
        a = math.sin(s/50)*200
        b =a+d
        pygame.display.update()
        print(a)


        
main()
