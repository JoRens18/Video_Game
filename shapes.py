import math
import pygame, sys
from pygame.locals import *


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
  def __init__(self,color, width, height):
    super(Ship,self).__init__()
    pygame.sprite.Sprite.__init__(self)
    self.Vx = 0
    self.Vy = 0
    self.image = pygame.image.load('images/ship.png')
    self.image = pygame.transform.scale(self.image,(130,57.5))
    self.rect = self.image.get_rect()
    self.rect.center = (750,500)

  def draw(self,surf):
    surf.blit(self.image,self.rect)

class Submarine(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    super(Submarine,self).__init__()
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('image/submarine.png')
    self.rect. = self.image.get_rect()
    self.rect.center = (500,750)
