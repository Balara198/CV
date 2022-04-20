import pygame, pygame.gfxdraw

pygame.init()
window = pygame.display.set_mode((320, 192))
pygame.display.set_caption('alpha')

window.blit(pygame.image.load('aaa.png'), (0,0))
pygame.display.update()
for y in range(192):
    for x in range(320):
        if window.get_at((x,y)) == (0,0,0,255):
            pygame.gfxdraw.pixel(window, x, y, pygame.Color('#ffffff00'))
pygame.display.update()
pygame.image.save(window, 'aaalpha.png')

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
