#import and set of variabls
import pygame as pg
import math
from pygame import  *
from math import  *
import sys

pg.init()

TITTLE = "my own grapher"

font = pg.font.SysFont('Verdana',16)
font2 = pg.font.SysFont('Serif', 24)
font3 = pg.font.SysFont('Arial', 14)

white = (255,255,255)
black = (0,0,0)
green = (70,159,29)
graphcolor = (200,0,200) #purple
gridcolor = (100,250,240) #light blue
titlecolor = (200,0,150)

width, height = 400 ,400
extraW = 400
screen = pg.display.set_mode((width + extraW, height))
