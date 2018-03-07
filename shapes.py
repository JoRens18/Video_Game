import math
import pygame, sys
from pygame.locals import *
import random

class Torpedo(pygame.sprite.Sprite):
  def __init__(self):
    super(Torpedo, self).__init__()
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('images/torpedo.png')
    self.image = pygame.transform.scale(self.image,(50,50))
    self.rect = self.image.get_rect()
    self.rect.center = (500,500)
  
  def draw(self, surf):
    surf.blit(self.image, self.rect)


class Ship(pygame.sprite.Sprite):
  def __init__(self):
    super(Ship,self).__init__()
    pygame.sprite.Sprite.__init__(self)
    self.Vx = 0
    self.Vy = 0
    self.image = pygame.image.load('images/ship.png')
    self.image = pygame.transform.scale(self.image,(130,58))
    self.rect = self.image.get_rect()
    self.x = random.randint(250,751)
    self.y = random.randint(250,751)
    self.rect.center = (self.x,self.y)

  def draw(self,surf):
    surf.blit(self.image,self.rect)

  def changeSpeed(self,dx,dy):
    self.Vx += dx
    self.Vy += dy
    
  def move(self):
    self.x += (self.Vx * (1.0/20))
    self.y += (self.Vy * (1.0/20))
    self.rect.center = (self.x,self.y)
    

class Submarine(pygame.sprite.Sprite):
  def __init__(self):
    super(Submarine,self).__init__()
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('images/submarine.png')
    self.rect = self.image.get_rect()
    self.rect.center = (500,750)
  
  def draw(self,surf):
    surf.blit(self.image,self.rect)



