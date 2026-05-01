import pygame
pygame.init()
x = 100
y = 100
screen = pygame.display.set_mode((400,500))
done = False
while not done:
    screen.fill((255,127,127))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        presses = pygame.key.get_pressed()
        if presses[pygame.K_UP]:
            y = y -5
        if presses[pygame.K_DOWN]:
            y = y +5
        if presses[pygame.K_LEFT]:
            x=x-5
        if presses[pygame.K_RIGHT]:
            x=x+5
    pygame.draw.rect(screen,'white', pygame.Rect(x,y,20,20))
    pygame.display.flip()        

        