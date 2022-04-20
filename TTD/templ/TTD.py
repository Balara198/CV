import pygame, pygame.gfxdraw, math, random, os

class Tile:
    def __init__(self, code, typ, height):
        self.code = code
        self.typ = typ
        self.height = height
            
        # t: Top, r: Right, b: Bottom, l: Left;  r: Realtive
        self.tr = int(code[0])
        self.rr = int(code[1])
        self.br = int(code[2])
        self.lr = int(code[3])
            
        self.t = int(code[0])+height
        self.r = int(code[1])+height
        self.b = int(code[2])+height
        self.l = int(code[3])+height
        
    def __str__(self):
        return '{} {} {}'.format(self.code, self.typ, self.height)
'''
class Tile:
    def __init__(self, code, typ, height):
        try:
            self.code = code
            self.typ = typ
            self.height = height
            
            # t: Top, r: Right, b: Bottom, l: Left;  r: Realtive
            self.tr = code[0]
            self.rr = code[1]
            self.br = code[2]
            self.lr = code[3]
            
            self.t = code[0]+height
            self.r = code[1]+height
            self.b = code[2]+height
            self.l = code[3]+height
        except:
            print('{} {} {}'.format(code, typ, height))
        
    def __str__(self):
        return '{} {} {}'.format(self.code, self.typ, self.height)
'''
'''
class map:
    def __init__(self):
        self.tiles = [['f' for i in range(10)] for j in range(10)]
        self.intersections[[0 for i in range(11)] for i in range(11)]
    def show(self, window, all_tiles):
        for iy, y in enumerate(self.tiles):
            for ix, xy in enumerate(y):
                tile_code = [self.intersections[iy]]
''' 
'''                
class Tile:
    def __init__(self, typ, height, x, y, corners):
        self.typ = typ
        self.height = height
        self.x = x
        self.y = y
        self.corners = corners
    def __str__(self):
        return '{}.png'.format([str(i) for i in self.corners].join(''))

class Map:
    def __init__(self):
        self.intersections = [[0 for i in range(11)] for i in range(11)]
        self.tiles = [[None for i in range(10)] for i in range(10)]
        for y in range(10):
            for x in range(10):
                corners = [self.intersections[y][x],
                           self.intersections[y+1][x+1],
                           self.intersections[y+2][x],
                           self.intersections[y+1][x],]
                tile_corners = [i-min(corners) for i in corners]
                self.tiles[y][x] = Tile(None, min(corners), x, y, tile_corners)
'''

def backgroundRemove(image):
    for y in range(192):
        for x in range(320):
            if image.get_at((x,y)) == (0,0,0,255):
                pygame.gfxdraw.pixel(image, x, y, pygame.Color('#ffffff00'))
                
    return image
    
def loadMap(name):
    game_map = []
    with open(name, 'rt') as f:
        for row in f:
            encoded = row.rstrip('\n').split(' ')
            decoded = [Tile(i[:4], i[4], int(i[5:])) for i in encoded]
            game_map.append(decoded)
    return game_map
    
def showMap(game_map, window, all_tiles, tile_indices):
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            window.blit(all_tiles, (32*(x-y+9), 16*(-1+x+y)-tile.height*8), pygame.Rect(tile_indices[tile.code], (64, 48)))
    pygame.display.update()
    
def recalculate(game_map, x, y):
    t = game_map[y][x]
    r = game_map[y][x+1]
    b = game_map[y+1][x+1]
    l = game_map[y+1][x]
    if True:
        return 1
        
def main():
    pygame.init()
    window = pygame.display.set_mode((640, 320))
    pygame.display.set_caption('Transport Tycoon Deluxe copy')
    
    all_tiles = pygame.image.load('new_conur.bmp')
    all_tiles.set_colorkey(pygame.Color('#c040c0'))
    tile_indices = {'0000' : (0,0), '0001' : (64,0), '0010' : (128,0), '0011' : (192,0), '0100' : (256,0),
                    '0101' : (0,48), '0110' : (64,48), '0111' : (128,48), '1000' : (192,48), '1001' : (256,48),
                    '1010' : (0,96), '1011' : (64,96), '1100' : (128,96), '1101' : (192,96), '1110' : (256,96),
                    '0121' : (0,144), '1012' : (64,144), '1210' : (128,144), '2101' : (192,144)} 
    '''
    game_map = [[Tile('0000', None, 0) for i in range(100)] for i in range(100)]
    game_map[5][5] = Tile('0010', None, 0)
    game_map[5][6] = Tile('0011', None, 0)
    game_map[5][7] = Tile('0001', None, 0)
    game_map[6][5] = Tile('0110', None, 0)
    game_map[6][6] = Tile('0000', None, 1)
    game_map[6][7] = Tile('1001', None, 0)
    game_map[7][5] = Tile('0110', None, 0)
    game_map[7][6] = Tile('0000', None, 1)
    game_map[7][7] = Tile('1001', None, 0)
    game_map[8][5] = Tile('0100', None, 0)
    game_map[8][6] = Tile('1100', None, 0)
    game_map[8][7] = Tile('1000', None, 0)
    '''
    game_map = loadMap('map.txt')
    
    showMap(game_map, window, all_tiles, tile_indices)

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
main()