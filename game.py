#!/usr/bin/python

#import system modules
import pygame, sys
from pygame.locals import *
import random 
import time

#import custom modules 
#import battle_ship
#import submarine
#import ocean

from color import *

#set up Window

pygame.init()
window = pygame.display.set_mode((1000,1000),0,32)

#set up FPS
fpsClock = pygame.time.Clock()
FPS = 120

#Drawing world 
def draw_world(surf):
  surf.fill(NAVYBLUE)
  pygame.display.update()

while(True):
	draw_world(window)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	pygame.display.update()
	fpsClock.tick(FPS)

	
