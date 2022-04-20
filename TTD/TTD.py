import pygame, pygame.gfxdraw

class Tile:
    def __init__(self, t, r, b, l, typ):
        self.t = t
        self.r = r
        self.b = b
        self.l = l
        self.typ = typ
    def kirajzol(self, x, y):
        mini = min(self.t, self.r, self.b, self.l)
        temp = str(self.t-mini) + str(self.r-mini) + str(self.b-mini) + str(self.l-mini)
        picString = self.typ + temp + '.png'

        
def main():
    pygame.init()
    window = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('PYGAME TESZT')
    isQuit = str(input("q;Q: quit, else continue")).lower() in "qQ"
    if isQuit:
        main()
main()


