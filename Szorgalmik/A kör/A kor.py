import pygame, pygame.gfxdraw, math

class Pont:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, rhs):
        return Pont(self.x-rhs.x, self.y-rhs.y)
    def __abs__(self):
        return int(math.sqrt(self.x**2 + self.y**2))

def akkora_tavra(p1, p2, tav, eps):
    return abs(abs(p1-p2)-tav) <= eps

class Kor:
    def __init__(self, K, r):
        self.K = K
        self.r = r
    def kirajzol(self, window):
        x, y = self.K.x, self.K.y
        pygame.gfxdraw.circle(window, x, y, self.r, pygame.Color('#ff0000'))
        pygame.gfxdraw.pixel(window, x, y, pygame.Color('#ff0000'))
        pygame.display.update()
        return
    
def main():
    pygame.init()
    window = pygame.display.set_mode((2560, 1440))
    pygame.display.set_caption('A kör')
    
    eps = 5
    kor = Kor(Pont(1280, 720), 100)
    kor.kirajzol(window)
    
    nem_katt = 0
    kozepre_katt = 1
    korivre_katt = 2
    allapot = nem_katt
    
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        if allapot == nem_katt:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = Pont(event.pos[0], event.pos[1])
                if akkora_tavra(kor.K, pos, 0, eps):
                    allapot = kozepre_katt
                elif akkora_tavra(kor.K, pos, kor.r, eps):
                    allapot = korivre_katt
        elif allapot == kozepre_katt:
            if event.type == pygame.MOUSEBUTTONUP:
                allapot = nem_katt
            elif event.type == pygame.MOUSEMOTION:
                pos = Pont(event.pos[0], event.pos[1])
                window.fill(pygame.Color('#000000'))
                kor.K = pos
                kor.kirajzol(window)
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                allapot = nem_katt
            elif event.type == pygame.MOUSEMOTION:
                pos = Pont(event.pos[0], event.pos[1])
                window.fill(pygame.Color('#000000'))
                kor.r = abs(kor.K-pos)
                kor.kirajzol(window)
    pygame.quit()
main()