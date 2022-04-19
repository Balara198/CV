import pygame, pygame.gfxdraw, math

def mandel(c, iter_depth):
    Z = c
    for i in range(iter_depth):
        if abs(Z) > 2:
            #print(Z)
            return False
        Z = Z**2+c
    return True

def main():
    pygame.init()
    r = 250

    x = 1500
    y = 1000
    
    win = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Mandelbrot_test_1')

    re = -2
    im = -1

    delta = 0.002

    min_iter_depth = 30
    max_iter_depth = 0
    delta_iter_depth = -1
    steps = (max_iter_depth-min_iter_depth)/delta_iter_depth
    delta_r = int(r/steps)
    
    for iter_depth in range(min_iter_depth, max_iter_depth, delta_iter_depth):
        for ix in range(x):
            for iy in range(y):
                if not mandel(complex(re+ix*delta, im+iy*delta), iter_depth):
                    pygame.gfxdraw.pixel(win, ix, iy, pygame.Color(r, 0, 0))
            
        pygame.display.update()
        print(f'{iter_depth}/{max_iter_depth}')
        r -= delta_r
        
    input('Nyomj gombot a kilépéshez!')
    pygame.quit()
    
main()
