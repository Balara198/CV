import serial, os, time
from kiir import *

def cls(n = 0):
    if n == 0:
        os.system('cls')
    else:
        print('\b'*n)
        
ser = serial.Serial('COM3', baudrate = 115200, timeout = 1)

arduinoData = ser.readline()
arduinoData = ser.readline()
while True:
    n = 0
    arduinoData = int(str(ser.readline())[8:-7])
    kep = dekodol(arduinoData, 3)
    cls(n)
    n = len(kep)
    print(kep)
