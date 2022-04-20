from math import *
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
    #print('PA: {:.1f}, PB: {:.1f}, AB: {:.1f} | P({:.1f},{:.1f}), B({:.1f},{:.1f}), A({:.1f},{:.1f}) | α: {:.1f}, β: {:.1f} | '.format(PA,PB,AB,Px,Py,Bx,By,Ax,Ay,α,β),end = ' | ')
    if α > pi/2 or β > pi/2:
        return PA if PA<PB else PB
    else:
        return m
        
def main():
    #print(pont_szakasz_tav(552.7,-224.2,7.1,-3.0,-252.7,242.2))
    #print(pont_szakasz_tav(300,18,-252.7,242.2,-245.7,239.2))
    print(pont_szakasz_tav(300,18,-252.7,242.2,-245.7,239.2))
main()