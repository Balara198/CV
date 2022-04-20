from math import *
from time import sleep
import pygame, pygame.gfxdraw

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __abs__(self):
        return sqrt( self.x**2 + self.y**2 )
    def __add__(self, rhs):
        return Point(self.x+rhs.x, self.y+rhs.y)
    def __iadd__(self, rhs):
        return self+rhs
    def __sub__(self, rhs):
        return Point(self.x-rhs.x, self.y-rhs.y)
    def __mul__(self, rhs):
        if type(rhs) in (int, float):
            return Point(self.x*rhs, self.y*rhs)
        else:
            return None
    def __round__(self):
        return Point(round(self.x), round(self.y))
    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)
'''
class Velocity:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction
    def toVector(self):
        tmp = self.magnitude/abs(self.direction)
        return direction*tmp
    def __add__(self, rhs):
        v = self.toVector() + rhs.toVector()
        return Velocity(abs(v), v)
    def __iadd__(self, rhs):
        return self + rhs
'''
class OBJ:
    def __init__(self, centre, radius, velocity, mass, color):
        self.centre = centre
        self.radius = radius
        self.velocity = velocity
        self.mass = mass
        self.color = color
    def distance(self, rhs):
        return abs(self.centre-rhs.centre)
    def accelerate(self, G, other):
        direction = other-self.centre
        magnitude = G/self.mass
        self.velocity += dirAndLenToVector(direction, magnitude)
        return self
    def draw(self, window):
        centre = round(self.centre)
        pygame.gfxdraw.filled_circle(window, centre.x, centre.y, self.radius, pygame.Color(self.color))
        return
    
def dirAndLenToVector(direction, magnitude):
    return direction*(magnitude/abs(direction))

def accelerate(objs):
    for i, obj in enumerate(objs):
        others = objs[:i]+objs[i+1:]
        others = [(other, (obj.mass * other.mass)/obj.distance(other)**2) for other in others]
        for other in others:
            obj.accelerate(other[1], other[0].centre)
    for obj in objs:
        obj.centre += obj.velocity
    return
    
def drawAll(objs, window):
    for obj in objs:
        obj.draw(window)
    return
    
def main():
    pygame.init()
    window = pygame.display.set_mode((1000,1000))
    blank = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('alma')
    o1 = OBJ(Point(500,10), 10, Point(0.06,0.01), 2, '#00ff00')
    o2 = OBJ(Point(200, 600), 16, Point(-0,0), 6, '#ff0000')
    o3 = OBJ(Point(500, 500), 6, Point(-0.12, -0.02), 1, '#0000ff')
    o4 = OBJ(Point(300, 700), 20, Point(0, 0), 10, '#ffff00')
    o5 = OBJ(Point(500, 250), 20, Point(0.05,0), 6, '#ff00ff')
    o6 = OBJ(Point(500, 750), 20, Point(-0.05,0), 6, '#00ffff')
    o7 = OBJ(Point(250, 500), 20, Point(0,-0.05), 6, '#00ffff')
    o8 = OBJ(Point(750, 500), 20, Point(0,0.05), 6, '#00ffff')
    o9 = OBJ(Point(500, 500), 6, Point(0,0), 1, '#0000ff')
    i = 0
    objs = [o1, o2, o5, o6]
    while True:
        pygame.gfxdraw.box(window, pygame.Rect(0, 0, 1920, 1080), pygame.Color('#ffffff'))
        
        accelerate(objs)
        drawAll(objs, window)
        '''
        G = (o1.mass * o2.mass)/o1.distance(o2)**2
        o1.accelerate(G, o2.centre)
        o2.accelerate(G, o1.centre)
        o1.centre += o1.velocity
        o2.centre += o2.velocity
        
        o1.draw(pygame.Color('#333333'), window)
        o2.draw(pygame.Color('#eeeec4'), window)
        print(i)
        print(o1.centre.x, end='  ')
        print(o1.centre.y)
        print(G)
        '''
        i+=1
        if i%40 == 0:
            pygame.display.update()
        
main()
    