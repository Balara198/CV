import pygame, pygame.gfxdraw, math, os

class Tile:
    def __init__(self, code, typ, height):
        self.code = code
        self.typ = typ
        self.height = height
    def __str__(self):
        return '{} {} {}'.format(self.code, self.typ, self.height)

def openMap(file_name):
    height_map = []
    tile_type_map = []
    with open(file_name, 'rt') as f:
        for i, row in enumerate(f):
            if i%2:
                tile_type_map.append(row.rstrip('\n').split(' '))
            else:
                height_map.append(row.rstrip('\n').split(' '))
    return height_map, tile_type_map

def mergeMaps(height_map, tile_type_map):
    tile_map = []
    for y, row in enumerate(tile_type_map):
        new_row = []
        for x, tile in enumerate(row):
            corners = [height_map[y][x],
                       height_map[y][x+1],
                       height_map[y+1][x],
                       height_map[y+1][x+1]]
            height = min(corners)
            code = [str(i-height) for i in corners].join('')
            new_row.append(Tile(code, tile, height))
        tile_map.append(new_row)
    return tile_map
    
def showMap(tile_map, window)