import pygame
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"

#to improve with inheritance principles
#to simplify when getting images


class LargeCactus:
  def __init__(self, width, option):
    #img_path = "img/3. Obstacles/"
    if option ==1:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/LargeCactus1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/LargeCactus2.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/LargeCactus3.png")),
      ]
    elif option ==2:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BigObs1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BigObs2.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BigObs3.png")),
      ]
    else:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BigPipe1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BigPipe2.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BigPipe3.png")),
      ]
    self.type = random.randint(0, 2)
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width*1.5
    self.rect.y = 380 - self.image[self.type].get_height()


  def update(self, speed, obstacles):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()

  def draw(self, screen):
    #print(self.rect.x)
    screen.blit(self.image[self.type], self.rect)


class SmallCactus:
  def __init__(self, width, option):
    if option == 1:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallCactus1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallCactus2.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallCactus3.png")),
      ]
    elif option == 2:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallObs1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallObs2.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallObs3.png")),
      ]
    else:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallGoomba1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallGoomba2.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/SmallGoomba3.png")),
      ]
    self.type = random.randint(0, 2)
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width*1.5
    self.rect.y = 380 - self.image[self.type].get_height()

  def update(self, speed, obstacles):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()

  def draw(self, screen):
    #print(self.rect.x)
    screen.blit(self.image[self.type], self.rect)


class Bird:
  BIRD_HEIGHT = [250, 290, 300]

  def __init__(self, width, option):
    self.flap = 0
    if option == 1:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/Bird1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/Bird2.png")),
      ]
    elif option == 2:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/FlyingPoke1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/FlyingPoke2.png")),
      ]
    else:
      self.image = [
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BulletBill1.png")),
          pygame.image.load(os.path.join(
              IMAGE_PATH, "3. Obstacles/BulletBill2.png")),
      ]
    self.type = 0
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width*1.5
    self.rect.y = random.choice(self.BIRD_HEIGHT)

  def update(self, speed, obstacles):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()

  def draw(self, screen):
    #print(self.flap )
    if self.flap >= 17:
      self.flap = 0
    screen.blit(self.image[self.flap //9], self.rect)
    self.flap += 1








