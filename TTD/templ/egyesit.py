import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((320, 288))
    pygame.display.set_caption('egyesito')
    
    uj = pygame.Surface((320, 192))
    x = 0
    y = 0
    for i in range(15):
        x = i%5
        y = i//5
        f = str(0)*(4-len(bin(i)[2:]))+bin(i)[2:]+'.png'
        print(f)
        uj.blit(pygame.image.load(f), (x*64,y*48))
    x = 0
    y = 3
    nevek = ['0121.png', '1012.png', '1210.png', '2101.png']
    for i in range(4):
        x = i%5
        uj.blit(pygame.image.load(nevek[i]), (x*64, y*48))
    pygame.image.save(uj, 'uj.png')
        
main()