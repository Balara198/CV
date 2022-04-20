import pygame
import pygame.gfxdraw
import menu_kezelo
import jatek_kezelo
import palya_valaszt
from BLOKK import Blokk

def main():

    pygame.init()
    window = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('laser-maze')

    menu_kezelo.kirajzol('fomenu', window)
    aktual_menu = menu_kezelo.megnyit('fomenu', window)
    
    KILEPES = False
    while KILEPES != True:
        if aktual_menu in ['fomenu', 'palyamenu', 'jatekmenu', 'gyozelem', 'vereseg']:
            menu_kezelo.kirajzol(aktual_menu, window)
            aktual_menu = menu_kezelo.megnyit(aktual_menu, window)
        elif aktual_menu == 'KILEPES':
            KILEPES = True
        else:
            if 'palya' in str(aktual_menu):
                valasztott = None
                jatekter, eszkoztar, start = palya_valaszt.betolt(aktual_menu)
                menu_kezelo.kirajzol('jatek_kepernyo', window)
                jatek_kezelo.palya_kirajzol(jatekter, window)
                jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                aktual_menu = menu_kezelo.megnyit('jatek_kepernyo', window)
                
            elif aktual_menu == 'SZIMULACIO':
                jatekter = jatek_kezelo.tovabbit(jatekter, start[0], start[1], jatekter[start[1]][start[0]].irany)
                jatek_kezelo.palya_kirajzol(jatekter, window)

                if jatek_kezelo.eredmeny(jatekter):
                    pygame.time.wait(20000)
                    menu_kezelo.kirajzol('gyozelem', window)
                    aktual_menu = menu_kezelo.megnyit('gyozelem', window)
                else:
                    pygame.time.wait(20000)
                    menu_kezelo.kirajzol('vereseg', window)
                    aktual_menu = menu_kezelo.megnyit('vereseg', window)

            elif aktual_menu == 'FOLYTAT':
                menu_kezelo.kirajzol('jatek_kepernyo', window)
                jatek_kezelo.palya_kirajzol(jatekter, window)
                jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                aktual_menu = menu_kezelo.megnyit('jatek_kepernyo', window)

            elif type(aktual_menu) is int:
                if aktual_menu < len(eszkoztar):
                    if valasztott is None or valasztott[1] == 'eszkozt.':
                        if valasztott is not None and valasztott[0] == aktual_menu:
                            valasztott = None
                            jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                        else:
                            valasztott = (aktual_menu, 'eszkozt.')
                            jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                            jatek_kezelo.eszkoztar_elem_kijelol(aktual_menu, window)
                    elif valasztott[0].fajta == 'ures':
                        jatekter[valasztott[3]][valasztott[2]] = eszkoztar[aktual_menu]
                        eszkoztar = eszkoztar[:aktual_menu] + eszkoztar[aktual_menu+1:]
                        valasztott = None
                        jatek_kezelo.palya_kirajzol(jatekter, window)
                        jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                    else:
                        valasztott = (aktual_menu, 'eszkozt.')
                        jatek_kezelo.eszkoztar_elem_kijelol(aktual_menu, window)
                        jatek_kezelo.palya_kirajzol(jatekter, window)
                aktual_menu = menu_kezelo.megnyit('jatek_kepernyo', window)

            elif type(aktual_menu) is tuple:
                temp = jatekter[aktual_menu[1]][aktual_menu[0]]
                if valasztott is None:
                    if temp.fajta in ['tukor', 'ures', 'f_tukor']:
                        valasztott = (temp, 'jatekt.', aktual_menu[0], aktual_menu[1])
                        jatek_kezelo.palya_blokk_kijelol(aktual_menu[0], aktual_menu[1], window)
                elif valasztott[1] == 'jatekt.':
                    if valasztott[0] != temp and temp.fajta in ['tukor', 'ures', 'f_tukor']:
                        jatekter[aktual_menu[1]][aktual_menu[0]] = jatekter[valasztott[3]][valasztott[2]]
                        jatekter[valasztott[3]][valasztott[2]] = temp
                        valasztott = None
                        jatek_kezelo.palya_kirajzol(jatekter, window)
                    else:
                        valasztott = None
                        jatek_kezelo.palya_kirajzol(jatekter, window)
                elif valasztott[1] == 'eszkozt.':
                    if temp.fajta == 'ures':
                        jatekter[aktual_menu[1]][aktual_menu[0]] = eszkoztar[valasztott[0]]
                        eszkoztar = eszkoztar[:valasztott[0]] + eszkoztar[valasztott[0]+1:]
                        valasztott = None
                        jatek_kezelo.palya_kirajzol(jatekter, window)
                        jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                    elif temp.fajta in ['tukor', 'ures', 'f_tukor']:
                            valasztott = (temp, 'jatekt.', aktual_menu[0], aktual_menu[1])
                            jatek_kezelo.palya_blokk_kijelol(aktual_menu[0], aktual_menu[1], window)
                    else:
                        valasztott = None
                    jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)

                aktual_menu = menu_kezelo.megnyit('jatek_kepernyo', window)

            elif aktual_menu == 'FORGAT':
                if valasztott is None:
                    pass
                if valasztott[1] == 'eszkozt.':
                    valasztott = None
                    jatek_kezelo.eszkoztar_kirajzol(eszkoztar, window)
                elif valasztott[0].fajta in ['tukor', 'f_tukor']:
                    temp = jatekter[valasztott[3]][valasztott[2]]
                    irany = (temp.irany+1)%4
                    jatekter[valasztott[3]][valasztott[2]] = Blokk(temp.fajta, irany)
                    valasztott[0].irany = irany
                    jatek_kezelo.palya_kirajzol(jatekter, window)
                    jatek_kezelo.palya_blokk_kijelol(valasztott[2], valasztott[3], window)
                aktual_menu = menu_kezelo.megnyit('jatek_kepernyo', window)

    pygame.quit()

main()
