import pygame
import pygame.gfxdraw


def main():
    pygame.init()
    window = pygame.display.set_mode((1200, 1788))
    pygame.display.set_caption('Leonardo')

    kep = pygame.image.load('a.png')
    window.blit(kep1, (0, 0))

    for x in range(1200):
        for y in range(1788):
            szin = window.get_at((x, y))[:3]
            if szin[0] in range(120, 190) and szin[1] in range(120, 190):
                pygame.gfxdraw.pixel(window, x, y, kever(szin, szin2))
        pygame.display.update()

main()
