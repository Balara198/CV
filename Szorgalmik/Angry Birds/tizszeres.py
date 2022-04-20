import turtle
from math import *


def radian(α):
    return α%360/180*pi

def pont_eltol(x,y,α,l):
    return x+l*cos(α), y+l*sin(α)
    
def ket_pont_tav(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def pont_szakasz_tav(Px,Py,Ax,Ay,Bx,By):
    PA = ket_pont_tav(Px,Py,Ax,Ay)
    PB = ket_pont_tav(Px,Py,Bx,By)
    AB = ket_pont_tav(Ax,Ay,Bx,By)
    
    Px -= Ax
    Bx -= Ax
    Py -= Ay
    By -= Ay

    α = acos((Px*Bx + Py*By)/(PA*AB))
    m = PA*sin(α)
    β = asin(m/PB)
    if α + β < pi:
        β = pi-β    
    if α > pi/2 or β > pi/2:
        return PA if PA<PB else PB
    else:
        return m
        
def kor_kirajzol(Ox,Oy,szinek,r):
    turtle.goto(Ox,Oy-r)
    if len(szinek) == 14:
        turtle.color(szinek[7:],szinek[:7])
        turtle.width(2)
        turtle.down()
    else:
        turtle.color(szinek)
    turtle.begin_fill()
    turtle.circle(r,360,int(24*r))
    turtle.end_fill()
    turtle.up()
    
    
def sokszog_kirajzol(x,y,szinek,pontok):
    turtle.goto(pontok[-1][0]+x,pontok[-1][1]+y)
    if len(szinek) == 14:
        turtle.color(szinek[:7],szinek[7:])
        turtle.width(2)
        turtle.down()
    else:
        turtle.color(szinek)
    turtle.begin_fill()
    for pont in pontok:
        turtle.goto(pont[0]+x,pont[1]+y)
    turtle.end_fill()
    turtle.up()
    
    
def alakzat_kirajzol(alakzat, x, y):
    for alak in alakzat:
        tipus = alak[0]
        szinek = alak[1]
        tobbi = alak[2]
        if tipus == 'k':
            eltol_x = alak[3]
            eltol_y = alak[4]
            kor_kirajzol(x+eltol_x, y+eltol_y, szinek, tobbi)
        else:
            sokszog_kirajzol(x, y, szinek, tobbi)


def main():
    turtle.setup(1200,1200)
    turtle.setworldcoordinates(0,0,399,399)
    turtle.tracer(0)
    turtle.hideturtle()
    
    g = 9.81
    t = 0.1
    x0 = 37.175
    y0 = 36.775
    malac_x = 300
    malac_y = 18
    r = 5
    malac_r = 10
    
    taj = [
        ['s', '#D9F5FB', [(0,0),(0,400),(400,400),(400,0)]],
        ['s', '#058715', [(0,0),(0,10),(400,10),(400,0)]]]
    
    csuzli_hatso = [
        ['s', '#301708#a67035', [(38.0, 16.7),(40.5, 22.6),(41.3, 24.7),(42.3, 29.0),(42.3, 34.3),(42.6, 38.5),(42.7, 42.7),(44.7, 43.5),(46.3, 42.7),(46.8, 38.7),(46.7, 33.8),(45.7, 28.7),(44.3, 23.7),(42.0, 17.0),(42.3, 3.3),(38.3, 3.3)]],
        ['s', '#301708#54280F', [(42.3, 34.3),(42.6, 38.5),(43.3, 39.1),(45.4, 39.1),(46.8, 38.7),(46.7, 33.8),(45.1, 34.6),(43.5, 34.7)]]]

    csuzli_elso = [
        ['s', '#301708#a67035', [(35.9, 20.1),(34.1, 24.6),(32.8, 29.9),(32.3, 33.8),(31.5, 37.4),(31.5, 40.5),(31.3, 44.7),(33.5, 45.9),(35.3, 45.9),(36.6, 45.2),(37.3, 40.5),(37.2, 34.5),(37.7, 30.0),(38.5, 26.2),(39.8, 23.0),(40.5, 23.0),(40.5, 21.6),(38.0, 16.7)]],
        ['s', '#301708#54280F', [(32.3, 33.8),(31.5, 37.4),(31.5, 40.5),(33.3, 40.1),(35.3, 40.2),(37.3, 40.5),(37.2, 34.5),(35.5, 33.8),(33.5, 33.7)]]]

    madar = [
        ['k', '#956F55', r,0,0],
        ['k', '#956F55', r,0,0.2],
        ['s', '#956F55', [(-4.3,2.5),(-2.4,6.1),(-1,5.1),(0,5.2),(1,5.1),(2.4,6.1),(4.3,2.5)]],
        ['k', '#FDFAE7', 1.8,2.1,2.3],
        ['k', '#FDFAE7', 1.8,-2.1,2.3],
        ['k', '#000000', 0.3,2.1,1.8],
        ['k', '#000000', 0.3,-2.1,1.8],
        ['s', '#F02020', [(-0.4,-0.9),(-3.2,0.1),(-3.2,-3.5),(-0.4,-4.3),(0.4,-4.3),(3.2,-3.5),(3.2,+0.1),(0.4,-0.9)]],
        ['s', '#674C39', [(-4.9,1.1),(-5.6,0.1),(-5.7,-0.1),(-5.7,-0.8),(-5.5,-1.3),(-4.9,-1.9),(-4.2,-2.3),(-2.5,-2.8),(-2.6,-1.8),(-3.1,-0.8),(-3.9,0.1)]],
        ['s', '#674C39', [(4.9,1.1),(5.6,0.1),(5.7,-0.1),(5.7,-0.8),(5.5,-1.3),(4.9,-1.9),(4.2,-2.3),(2.5,-2.8),(2.6,-1.8),(3.1,-0.8),(3.9,0.1)]],
        ['s', '#F8A73F', [(0,0.6),(0.4,1),(0,1.3),(-0.4,1)]]]
    
    malac = [
        ['k', '#75E543', 10,0,0]]
    
    gumi = [
        ['s', '#301708#54280F', [(42.3, 34.3),(42.6, 38.5),(31.5, 37.4),(32.3, 33.8)]]]
    
    kosar = [['s', '#54280F', [  ]]]
    
    gyozelem = False
    V = None
    while not gyozelem:
        if V is None:
            V = turtle.numinput('kezdeti sebesség', 'Sebesség: ', 40, 20, 100)
            szog = turtle.numinput('Hajítási szög', 'Hajítási szög: (0-nál ez keleti irányba mutat)', 0, 0)
        else:
            V = turtle.numinput('kezdeti sebesség', 'Sebesség: ', V, 20, 100)
            szog = turtle.numinput('Hajítási szög', 'Hajítási szög: (0-nál ez keleti irányba mutat)', szog, 0)
        α = radian(szog)
        x,y = pont_eltol(x0,y0,pi+α,3.5*sqrt(V))
        Vx = V*cos(α)
        Vy = V*sin(α)
        temp = kosar[0][2]
        roppalya_1 = []
        roppalya_2 = [(x0,y0)]
        for i in range(4):
            kosar[0][2].append(pont_eltol(0,0,(α+pi)+radian(30-20*i),5.1))
        kosar[0][2].append((0,0))
        gumi_hatso = [
            ['s', '#54280F', [(42.3, 34.3),(42.6, 38.5),(temp[-2][0]+x,temp[-2][1]+y),(temp[-1][0]+x,temp[-1][1]+y),(temp[0][0]+x,temp[0][1]+y)]]]
        
        gumi_elso = [
            ['s', '#54280F', [(32.3, 33.8),(31.5, 37.4),(temp[-2][0]+x,temp[-2][1]+y),(temp[-1][0]+x,temp[-1][1]+y),(temp[0][0]+x,temp[0][1]+y)]]]

        kiloves = True
        while kiloves:
            turtle.clear()
            if ket_pont_tav(x0,y0,x,y) <= V*t:
                kiloves = False
            if 1/2*pi <= α < 3/2*pi:
                temp = gumi_hatso[0][2][-1]
                gumi_hatso[0][2][-1] = gumi_hatso[0][2][-3]
                gumi_hatso[0][2][-3] = temp
                temp = gumi_elso[0][2][-1]
                gumi_elso[0][2][-1] = gumi_elso[0][2][-3]
                gumi_elso[0][2][-3] = temp
            for i in range(3):
                temp = gumi_hatso[0][2][-i-1]
                gumi_hatso[0][2][-i-1] = (temp[0] + Vx*t, temp[1] + Vy*t)
                temp = gumi_elso[0][2][-i-1]
                gumi_elso[0][2][-i-1] = (temp[0] + Vx*t, temp[1] + Vy*t)
            alakzat_kirajzol(taj,0,0)
            alakzat_kirajzol(csuzli_hatso,0,0)
            alakzat_kirajzol(gumi_hatso,0,0)
            alakzat_kirajzol(malac,malac_x,malac_y)
            if kiloves:
                roppalya_1.append((x,y))
            else:
                roppalya_1.append((x0,y0))
            if len(roppalya_1) > 1:
                turtle.color('#DDDD11')
                turtle.goto(roppalya_1[0])
                turtle.width(5)
                turtle.down()
                for pont in roppalya_1:
                    turtle.goto(pont)
                turtle.up()
            alakzat_kirajzol(madar,x,y)
            alakzat_kirajzol(kosar,x,y)
            alakzat_kirajzol(gumi_elso,0,0)
            alakzat_kirajzol(csuzli_elso,0,0)
            turtle.update()            
            x += Vx*t
            y += Vy*t
        

        x = x0
        y = y0
        repul = True
        while repul:
            turtle.clear()
            Vy -= g*t
            elozo_x = x
            elozo_y = y
            y += t*Vy
            x += t*Vx
            if not gyozelem:
                gyozelem = pont_szakasz_tav(malac_x,malac_y,x,y,elozo_x,elozo_y) <= r+malac_r
            if y <= 8:
                repul = False
                y = 8
                x = elozo_x
            roppalya_2.append((x,y))
            alakzat_kirajzol(taj,0,0)
            alakzat_kirajzol(csuzli_hatso,0,0)
            alakzat_kirajzol(gumi,0,0)
            turtle.color('#DDDD11')
            turtle.goto(roppalya_1[0])
            turtle.width(5)
            turtle.down()
            for pont in roppalya_1:
                turtle.goto(pont)
            turtle.up()
            if len(roppalya_2) > 1:
                turtle.color('#FF2311')
                turtle.goto(roppalya_2[0])
                turtle.width(5)
                turtle.down()
                for pont in roppalya_2:
                    turtle.goto(pont)
                turtle.up()
            if not gyozelem:
                alakzat_kirajzol(malac,malac_x,malac_y)
            alakzat_kirajzol(madar,x,y)
            alakzat_kirajzol(csuzli_elso,0,0)
            turtle.update()
    print('Győzelem!')

main()