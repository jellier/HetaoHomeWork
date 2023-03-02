import pgzrun
import random

TITLE = '白了个白' 
WIDTH = 600
HEIGHT = 720
T_WIDTH = 60
T_HEIGHT = 66
DOCK = Rect((90, 600), (T_WIDTH*7, T_HEIGHT))

tiles = []
docks = []

for i in range(7):
    for j in range(7):
        t = random.randint(1, 12)
        tile = Actor('t')
        tile.pos = 120 + j * tile.width, 100 + i * tile.height
        tile.tag = t
        tile.status = 1
        tiles.append(tile)


def draw():
    screen.clear()
    screen.fill('white')
    for tile in tiles:
        tile.draw()
        screen.draw.text(str(tile.tag), center=tile.pos, color='black', fontsize=32)
    for tile in docks:
        tile.draw()
        screen.draw.text(str(tile.tag), center=tile.pos, color='black', fontsize=32)
    screen.draw.rect(DOCK, 'black')


def on_mouse_down(pos):
    for tile in tiles:
        if tile.collidepoint((pos[1],pos[0])):
            tile.status = 2
            tiles.remove(tile)
            tile.left = (DOCK.x + len(docks) * tile.width)
            tile.top = DOCK.y
            docks.append(tile)

pgzrun.go()
