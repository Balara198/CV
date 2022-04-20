import pygame
import pygame.gfxdraw


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('színek szorzása')

    kep1 = pygame.image.load('jatekmenu.png')
    window.blit(kep1, (0, 0))

    for x in range(800):
        for y in range(700):
            szin = window.get_at((x, y))[:3]
            szin1 = pygame.Color(226, 226, 226)
            szin2 = pygame.Color(195, 195, 195)
            szin3 = pygame.Color(127, 127, 127)
            if szin[2] < 45:
                pygame.gfxdraw.pixel(window, x, y, szin3)
            elif szin[2] > 140:
                pygame.gfxdraw.pixel(window, x, y, szin1)
            else:
                pygame.gfxdraw.pixel(window, x, y, szin2)
    pygame.display.update()

main()
