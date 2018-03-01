import math
import pygame, sys
from pygame.locals import *


class Torpedo(pygame.sprite.Sprite):
  def __init__(self):
    super(Torpedo, self).__init__()
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('images/torpedo.png')
    self.rect = self.image.get_rect()
    self.rect.center = (500,500)
  
  def draw(self, surf):
    surf.blit(self.image, self.rect)


class Ship(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.image = images/ship

class Submarine(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.image = images/submarine
