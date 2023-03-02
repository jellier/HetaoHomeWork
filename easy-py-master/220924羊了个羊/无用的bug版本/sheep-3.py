import pgzrun
import pygame
import random
import math
import os

TITLE = '白了个白' 
WIDTH = 600
HEIGHT = 720
T_WIDTH = 60
T_HEIGHT = 66
DOCK = Rect((90, 600), (T_WIDTH*7, T_HEIGHT))

tiles = []
docks = []

for k in range(5):
    for i in range(7):
        for j in range(7):
            t = random.randint(1, 12)
            tile = Actor('t')
            tile.pos = 120 + j * tile.width, 100 + i * tile.height
            tile.tag = t
            tile.layer = k
            tile.status = 1
            tiles.append(tile)


def draw():
    screen.clear()
    screen.fill('white')
    for tile in tiles:
        tile.draw()
        screen.draw.text(str(tile.tag), center=tile.pos, color='black', fontsize=32)
    for i, tile in enumerate(docks):
        tile.left = (DOCK.x + i * T_WIDTH)
        tile.top = DOCK.y
        tile.draw()
        screen.draw.text(str(tile.tag), center=tile.pos, color='black', fontsize=32)
    screen.draw.rect(DOCK, 'black')


def on_mouse_down(pos):
    global docks
    for tile in reversed(tiles):
        if tile.collidepoint(pos):
            tile.status = 2
            tiles.remove(tile)
            diff = [t for t in docks if t.tag != tile.tag]
            if len(docks) - len(diff) < 2:
                docks.append(tile)
            else:
                docks = diff
            return

pgzrun.go()


