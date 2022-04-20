import random
 
import pygame
import pygame.gfxdraw
 
 
def input_text(x, y, width, height, bg_color, fg_color, font, surface):
    clip = surface.get_clip()
    destination = pygame.Rect(x, y, width, height)
    surface.set_clip(destination)
 
    user_input = ''
    enter = False
    quit = False
    while (not quit) and (not enter):
        # szöveg kirajzolása
        pygame.gfxdraw.box(surface, destination, bg_color)
        pygame.gfxdraw.rectangle(surface, destination, fg_color)
        text = font.render(user_input + '|', True, fg_color)
        surface.blit(text, destination)
        pygame.display.update()
 
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            # enter: bevitel vége
            if event.key == pygame.K_RETURN:
                enter = True
            # backspace: utolsó karakter törlése
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            # egyébként meg hozzáadjuk a beírt szöveghez
            else:
                user_input += event.unicode
 
        if event.type == pygame.QUIT:
            # visszatesszük a sorba, mert sok mindent nem tudunk vele kezdeni
            pygame.event.post(event)
            quit = True
 
    surface.set_clip(clip);
    return user_input
 
 
def randomcolor():
    return pygame.Color(random.randrange(256), random.randrange(256), random.randrange(256))
 
 
def main():
    white = pygame.Color('#FFFFFF')
    black = pygame.Color('#000000')
 
    pygame.init()
 
    window = pygame.display.set_mode((480, 200))
    pygame.display.set_caption('pygame szöveg bevitele')
 
    font = pygame.font.SysFont('Arial', 32)
 
    # szöveg beolvasása
    for i in range(200):
        pygame.gfxdraw.filled_circle(window,
                                     random.randrange(480),
                                     random.randrange(200),
                                     random.randrange(20, 25),
                                     randomcolor())
    pygame.display.update()
    user_input = input_text(40, 80, 400, 40, black, white, font, window)
 
    # szöveg kirajzolása
    pygame.gfxdraw.box(window, pygame.Rect(0, 0, 480, 200), black)
    for i in range(200):
        pygame.gfxdraw.filled_circle(window,
                                     random.randrange(480),
                                     random.randrange(200),
                                     random.randrange(20, 25),
                                     randomcolor())
    text = font.render(user_input, True, white)
    window.blit(text, ((480 - text.get_width()) / 2, (200 - text.get_height()) / 2))
    pygame.display.update()
 
    quit = False
    while not quit:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            quit = True
 
    pygame.quit()
 
 
main()
