import serial
import pygame
import pygame.gfxdraw


def main():
    pygame.init()
    window = pygame.display.set_mode((255, 255))
    pygame.display.set_caption('Joystick')

    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    white = pygame.Color(255, 255, 255)
    
    ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

    arduinoData = ser.readline()
    arduinoData = ser.readline()
    while True:

        pygame.gfxdraw.box(window,(0, 0, 255, 255), white)
        
        arduinoData = ser.readline()
        temp = str(arduinoData)[2:-5]
        temp = temp.split('x')
        print('x:{}; y:{}; button:{}'.format(temp[0],temp[1],temp[2]))


        x = abs(int(temp[0])-255)
        y = int(temp[1])
        b = int(temp[2])
        if b:
            pygame.gfxdraw.box(window, (x-2, y-2, 5, 5), red)
        else:
            pygame.gfxdraw.box(window, (x-2, y-2, 5, 5), green)
        pygame.display.update()
        
main()
