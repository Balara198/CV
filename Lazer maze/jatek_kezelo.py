import pygame
from BLOKK import Blokk


def fajtabol_kep(fajta):
    return pygame.image.load('{}.png'.format(fajta))

def eredmeny(jatekter):
    for y in jatekter:
        for x in y:
            if x.fajta == 'stop':
                return False
    return True
                

def blokk_kirajzol(blokk, x, y, window):
    window.blit(
        pygame.transform.rotate(
            fajtabol_kep(blokk.fajta), blokk.irany*-90), (x*100, y*100))
    pygame.display.update()

def palya_kirajzol(jatekter, window):
    for y in range(len(jatekter)):
        for x in range(len(jatekter[y])):
            blokk_kirajzol(jatekter[y][x], x+1.4, y+1, window) #mivel a függvény a koordináták 100-szorosá veszi, ezért a 100, 140-es eltolás a paraméterben +1 és +1.4 értékű
    pygame.display.update()

def eszkoztar_kirajzol(eszkoztar, window):
    for i in range(len(eszkoztar)):
        blokk_kirajzol(eszkoztar[i], 6.9, 5.5-i, window)
    ures = 6-len(eszkoztar)    
    window.blit(
        pygame.image.load('jatek_kepernyo.png'), (690, 50),
                pygame.Rect(
                    (690, 50), (790, 100*ures)))
    pygame.display.update()

def tovabbit(jatekter, x, y, irany):
    iranyok = [(y+1, x),(y, x-1),(y-1, x),(y, x+1)]
    if x in range(5) and y in range(5):
        fajta = jatekter[y][x].fajta
        elforagtas = jatekter[y][x].irany
        
        if fajta == 'start':
            jatekter[y][x] = Blokk('start-be', irany)
            jatekter = tovabbit(jatekter, iranyok[irany][1], iranyok[irany][0], irany)
        
        elif jatekter[y][x].fajta == 'ures':
            jatekter[y][x] = Blokk('laser', irany)
            jatekter = tovabbit(jatekter, iranyok[irany][1], iranyok[irany][0], irany)
        
        elif jatekter[y][x].fajta == 'tukor':
            if elforagtas%2 == 0:
                temp = 3-irany
                jatekter[y][x] = Blokk('I_laser_tukor', (irany//2)*2)
            else:
                temp = irany + (-1)**irany
                jatekter[y][x] = Blokk('I_laser_tukor', (irany-1)%4+irany%2)
            jatekter = tovabbit(jatekter, iranyok[temp][1], iranyok[temp][0], temp)
        
        elif fajta == 'I_laser_tukor':
            temp2 = 3-irany if elforagtas%2 == 0 else irany + (-1)**irany
            jatekter[y][x] = Blokk('II_laser_tukor', elforagtas)
            tovabbit(jatekter, iranyok[temp2][1], iranyok[temp2][0], temp2)

        elif fajta == 'f_tukor':
            temp = 3-irany if elforagtas%2 == 0 else irany + (-1)**irany
            if (elforagtas+irany)%2:
                jatekter[y][x] = Blokk('I_laser_f_tukor_inverz', irany)
            else:
                jatekter[y][x] = Blokk('I_laser_f_tukor', irany)
            jatekter = tovabbit(jatekter, iranyok[irany][1], iranyok[irany][0], irany)
            jatekter = tovabbit(jatekter, iranyok[temp][1], iranyok[temp][0], temp)

        elif fajta == 'I_laser_f_tukor':
            if irany != elforagtas:
                if (irany+1)%4 != elforagtas:
                    temp = (elforagtas+1)%4
                    jatekter = tovabbit(jatekter, iranyok[temp][1], iranyok[temp][0], temp)
                    temp = (temp+1)%4
                    jatekter = tovabbit(jatekter, iranyok[temp][1], iranyok[temp][0], temp)
                jatekter[y][x] = Blokk('II_laser_f_tukor', elforagtas)

        elif fajta == 'I_laser_f_tukor_inverz':
            if irany != elforagtas:
                if (irany-1)%4 != elforagtas:
                    temp = (elforagtas+3)%4
                    jatekter = tovabbit(jatekter, iranyok[temp][1], iranyok[temp][0], temp)
                    temp = (temp-1)%4
                    jatekter = tovabbit(jatekter, iranyok[temp][1], iranyok[temp][0], temp)
                jatekter[y][x] = Blokk('II_laser_f_tukor', elforagtas%2+1)
                    
        elif fajta == 'laser':
            jatekter = tovabbit(jatekter, iranyok[irany][1], iranyok[irany][0], irany)
            if irany%2 != elforagtas%2:
                jatekter[y][x] = Blokk('dupla_laser', irany)
        
        elif fajta == 'stop':
            jatekter[y][x] = Blokk('be_stop', irany)

    return jatekter

def eszkoztar_elem_kijelol(y, window):
    kijelolo_negyzet = (691, 550-y*100, 97, 97)
    pygame.draw.rect(window, pygame.Color('#00ff00'), kijelolo_negyzet, 3)
    pygame.display.update()
    return
def palya_blokk_kijelol(x, y, window):
	kijelolo_negyzet = (x*100+141, y*100+101, 97, 97)
	pygame.draw.rect(window, pygame.Color('#00ff00'), kijelolo_negyzet, 3)
	pygame.display.update()
	return