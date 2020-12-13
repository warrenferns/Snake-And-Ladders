import pygame
from random import randint
import time
import pyflakes

clock = pygame.time.Clock()

pygame.init()

w = 1366
h = 768

icon = pygame.image.load("icon.png")
GD = pygame.display.set_mode((w,h),pygame.FULLSCREEN)

pygame.display.set_caption("Snake N Ladders")
pygame.display.set_icon(icon)
pygame.display.set_update()

black = (10,10,10)
white = (250,250,250)
red = (200,0,0)
b_red = (240,0,0)
green = (0,200,0)
b_green = (0,230,0)
blue = (0,0,200)
grey = (50,50,50)
yellow = (150,150,0)
purple = (43,3,132)
b_purple = (60,0,190)

board = pygame.image.load("Snake-and-Ladders.jpg")
dice1 = pygame.image.load("Dice1.png")
dice2 = pygame.image.load("Dice2.png")
dice3 = pygame.image.load("Dice3.png")
dice4 = pygame.image.load("Dice4.png")
dice5 = pygame.image.load("Dice5.png")
dice6 = pygame.image.load("Dice6.png")

redgoti = pygame.image.load("redgoti.png")
yellowgoti = pygame.image.load("yellowgoti.png")
greengoti = pygame.image.load("greengoti.png")
bluegoti = pygame.image.load("bluegoti.png")
menubg = pygame.image.load("menu.png")
p = pygame.image.load("playbg.png")

intbg = pygame.image.load("intropic.jpg")
intbg2 = pygame.image.load("intropic2.jpg")
intbg3 = pygame.image.load("intropic3.jpg")
intbg4 = pygame.image.load("intropic4.jpg")
intbg5 = pygame.image.load("intropic5.jpg")

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

def message_display(text,x,y,fs):
  largeText = pygame.font.Font('freesansbold.ttf',fs)
  TextSurf, TextRect = text_objects(text, largeText)
  TextRect.center = (x,y)
  GD.blit(TextSurf, TextRect)
  
def text_objects(text,font):
  textSurface = font.render(text,True,white)
  return textSurface, textSurface.get_rect()

def message_display1(text,x,y,fs,c):
  largeText = pygame.font.Font('freesansbold.ttf',fs)
  TextSurf, TextRect = text_objects(text, largeText)
  TextRect.center = (x,y)
  GD.blit(TextSurf, TextRect)

def text_objects1(text,font,c):
  textSurface = font.render(text,True,c)
  return textSurface, textSurface.get_rect()

def goti(a):
  l1 = [[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]

  l2 = l1[a]
  x = l2[0] -25
  y = l2[1] - 25
  return x, y

def text_objects1(text,font):
  textSurface = font.render(text,True,black)
  return textSurface, textSurface.get_rect()

def ladders(x):
  if x==1: return 38
  elif x==4: return 14
  elif x==9: return 31
  elif x==28: return 24
  elif x==21: return 42
  elif x==51: return 67
  elif x==80: return 99
  elif x==72: return 91
  else: return x

def snakes(x):
  if x==17: return 7
  elif x==54: return 34
  elif x==62: return 19
  elif x==64: return 60
  elif x==87: return 36
  elif x==93: return 73
  elif x==95: return 75
  elif x==98: return 79
  else: return x 

def dice(a):
  if a==1:
    a = dice1
  elif a==2:
    a = dice2
  elif a==3:
    a = dice3
  elif a==4:
    a = dice4
  elif a==5:
    a = dice5
  elif a==6:
    a = dice6         

  time = pygame.time.get_ticks()
  while pygame.time.get_ticks() - time <1000:
    GD.blit(a,(300,500))
    pygame.display.update()

def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if x+w >xmouse >x and y+h >ymouse > y:
    pygame.draw.rect[GD,a,[x-2.5,y-2.5,w+5,h+5]]
    if pygame.mouse.get_pressed() == (1,0,0):
      return True
  else:
    pygame.draw.rect(GD, i, [x,y,w,h])
  message_display(text, (x+w+x)/2, (y+h+y)/2, fs)

def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if x+w >xmouse >x and y+h >ymouse > y:
    pygame.draw.rect[GD,a,[x-2.5,y-2.5,w+5,h+5]]
    if pygame.mouse.get_pressed() == (1,0,0):
      return True
  else:
    pygame.draw.rect(GD, i, [x,y,w,h])
  message_display(text, (x+w+x)/2, (y+h+y)/2, fs)


