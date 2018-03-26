#!/usr/bin/python

#import system modules
import pygame, sys
from pygame.locals import *
import random 
import time
import shapes
import serial


from color import *

#set up Window

pygame.init()

s = serial.Serial("/dev/ttyACM0")
window = pygame.display.set_mode((1000,1000),0,32)
pygame.display.set_caption('Enjoy your voyage!')
#set up FPS
fpsClock = pygame.time.Clock()
FPS = 60




ship = shapes.Ship()


#Drawing world 
def draw_world(surf):
  surf.fill(NAVYBLUE)
  ship.draw(surf)
  #submarine.draw(surf)


def displayMessage(surf, msg):
  # display [msg] for 1 second (freezes the game)
  fontObj = pygame.font.Font('freesansbold.ttf',40)
  textSurfaceObj = fontObj.render(msg,True, RED)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (500,250)
  surf.blit(textSurfaceObj,textRectObj)
  pygame.display.update()
  time.sleep(1)


while(True):
  fire = random.randint(0,100)  
  water = 0
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
  while(fire == 1 and water < 50):
    displayMessage(window,"Fire!")
    s.write('p')
    l=s.readline()
    if not len(l) == 0:
      water = int(l)
    
    


  ship.move()
  draw_world(window)
  pygame.display.update()
  fpsClock.tick(FPS)


	
