import pygame
import pygame.draw

pygame.init()
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption ("lumemees-Madis Plaks")
screen.fill([0,0,0])
pygame.draw.circle(screen, [255,255,255], [140,200], 50, )
pygame.draw.circle(screen, [255,255,255], [140,120], 40 )
pygame.draw.circle(screen, [255,255,255], [140,60], 30 )
pygame.draw.line(screen, [255,102,0],[133,60], [139,60], 3)
pygame.draw.circle(screen,[0,0,0],[145,47],5,0 )
pygame.draw.circle(screen,[0,0,0],[130,47],5,0 )
}
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        #  laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False