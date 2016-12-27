import pygame, sys
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Bounce')

background = pygame.Surface(screen.get_size())
width, height = pygame.display.get_surface().get_size()

FPS = 30 
fpsClock = pygame.time.Clock()

Black=(0,0,0)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)

SpeedX=0
SpeedY=10
PosX=width/2
PosY=height/2
flag=1

Ball_radius=Ball_width=30

while True:
    screen.blit(background,(0,0))
    if(flag==0):
	PosY+=SpeedY
        if(PosY>height-Ball_radius):
            flag=1
    else:
        PosY-=SpeedY
        if(PosY<height/2):
            flag=0
    pygame.draw.circle(screen,Red,(PosX,PosY),Ball_radius,Ball_width)
    for event in pygame.event.get():
	if event.type == QUIT:
		pygame.quit()
		sys.exit()
    background.fill(Green)
    pygame.display.update()
    fpsClock.tick(FPS)
