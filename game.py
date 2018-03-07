#!/usr/bin/python

#import system modules
import pygame, sys
from pygame.locals import *
import random 
import time
import shapes

#import custom modules 
#import battle_ship
#import submarine
#import ocean

from color import *

#set up Window

pygame.init()
window = pygame.display.set_mode((1000,1000),0,32)
pygame.display.set_caption('Avoid the Torpedos!')
#set up FPS
fpsClock = pygame.time.Clock()
FPS = 60

torpedo = shapes.Torpedo()
ship = shapes.Ship()
#submarine = shapes.Submarine()

#Drawing world 
def draw_world(surf):
  surf.fill(NAVYBLUE)
  ship.draw(surf)
  #submarine.draw(surf)
  

while(True):
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        ship.changeSpeed(0,-5)
      if event.key == pygame.K_DOWN:
        ship.changeSpeed(0,5)
      if event.key == pygame.K_RIGHT:
        ship.changeSpeed(5,0)
      if event.key == pygame.K_LEFT:
        ship.changeSpeed(-5,0)
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  ship.move()
  draw_world(window)
  pygame.display.update()
  fpsClock.tick(FPS)


	
