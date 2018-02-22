import math
import pygame, sys
from pygame.locals import *

class Torpedo(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.image = images/torpedo

class Ship(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.image = images/ship

class Submarine(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.image = images/submarine
