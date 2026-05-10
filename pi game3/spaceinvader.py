import math
import random
import pygame

Screen_width = 800
Screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_min = 150
enemy_speed_x = 4
enemy_speed_y = 20
bullet_speed_y = 20
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((Screen_width,Screen_height))
background = pygame.transform.scale(pygame.image.load("space.jpg").convert(),(Screen_width,Screen_height))


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    