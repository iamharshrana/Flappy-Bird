import pygame
import sys

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,440))
    screen.blit(floor_surface,(floor_x_pos + 288,440))



pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

#Game variable
gravity = 0.10
bird_movement = 0

bg_surface  = pygame.image.load('assets/background-night.png').convert()

floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (80,250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 4
    
    screen.blit(bg_surface,(0,0))

    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bird_surface,bird_rect)
    floor_x_pos += -1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0 
    
    
    pygame.display.update()
    clock.tick(120)