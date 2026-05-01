import pygame
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width,height))
screen.fill('yellow')
done = False
l = width//2
t = height//2
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,"navy",pygame.Rect((30,30),(70,50)))
    pygame.display.flip()