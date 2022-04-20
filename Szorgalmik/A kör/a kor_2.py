import pygame, pygame.gfxdraw, math

class Pont:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, rhs):
        return Pont(self.x-rhs.x, self.y-rhs.y)
    def __abs__(self):
        return int(math.sqrt(self.x**2 + self.y**2))


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

def akkora_tavra(p1, p2, tav, eps):
    return abs(abs(p1-p2)-tav) <= eps

def uj_kurzor(kurzor, hotspot):
    meret = len(kurzor[0]), len(kurzor)
    kurzor, maszk = pygame.cursors.compile(kurzor)
    pygame.mouse.set_cursor(meret, hotspot, kurzor, maszk)
    
def main():
    nyil = (
        "X                       ",
        "XX                      ",
        "X.X                     ",
        "X..X                    ",
        "X...X                   ",
        "X....X                  ",
        "X.....X                 ",
        "X......X                ",
        "X.......X               ",
        "X........X              ",
        "X.........X             ",
        "X..........X            ",
        "X......XXXXX            ",
        "X...X..X                ",
        "X..X X..X               ",
        "X.X  X..X               ",
        "XX    X..X              ",
        "      X..X              ",
        "       XX               ",
        "                        ",
        "                        ",
        "                        ",
        "                        ",
        "                        ",
        )
             
        
        
        
    ujj = [
        "     XX                 ",
        "    X..X                ",
        "    X..X                ",
        "    X..X                ",
        "    X..X                ",
        "    X..XXX              ",
        "    X..X..XXX           ",
        "    X..X..X..XX         ",
        "    X..X..X..X.X        ",
        "XXX X..X..X..X..X       ",
        "X..XX..X..X..X..X       ",
        "X...X........X..X       ",
        " X..............X       ",
        "  X.............X       ",
        "  X.............X       ",
        "   X............X       ",
        "   X...........X        ",
        "    X..........X        ",
        "    X..........X        ",
        "     X........X         ",
        "     X........X         ",
        "     XXXXXXXXXX         ",
        "                        ",
        "                        "
        ]
                   
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('A kör')
    
    kor = Kor(Pont(640, 360), 100)
    kor.kirajzol(window)
    #0-nem kattintott, 1-középpontra kattintott, 2-körívre kattintott
    allapot = 0
    eps = 5
    kurzor = 'nyil'
    uj_kurzor(nyil, (5, 0))
    while True:
        event = pygame.event.wait()
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            pos = Pont(event.pos[0], event.pos[1])
                
        if event.type == pygame.QUIT:
            break
        if allapot == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if akkora_tavra(kor.K, pos, 0, eps):
                    allapot = 1
                elif akkora_tavra(kor.K, pos, kor.r, eps):
                    allapot = 2
        elif allapot == 1:
            if event.type == pygame.MOUSEBUTTONUP:
                allapot = 0
            elif event.type == pygame.MOUSEMOTION:
                window.fill(pygame.Color('#000000'))
                kor.K = pos
                kor.kirajzol(window)
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                allapot = 0
            elif event.type == pygame.MOUSEMOTION:
                window.fill(pygame.Color('#000000'))
                kor.r = abs(kor.K-pos)
                kor.kirajzol(window)
    pygame.quit()
main()