import pygame, random
import pygame.gfxdraw

def main():
    pygame.init()
    window = pygame.display.set_mode((64, 40))
    pygame.display.set_caption('zajosítás')
    
    for i in range(15):
        nev = bin(i)[2:]
        f = '0'*(4-len(nev))+nev+'.png'
        
        kep = pygame.image.load(f)

        ujKep = pygame.Surface((64, 48))
        ujKep.blit(kep, (0,8))
        pygame.image.save(ujKep, f)
    

main()