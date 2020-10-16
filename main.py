import pygame
from pygame.draw import *
from random import randint

pygame.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 100
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

height = 800
width = 1000
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

bx, by, bvx, bvy, br, ballcolor = [], [], [], [], [], []


def new_ball():
    """рисует новый шарик """
    global bx, by, br, bvx, bvy, ballcolor
    bx.append(randint(100, width - 100))
    by.append(randint(100, height - 100))
    bvx.append(randint(1, 5) * (-1) ** randint(1, 2))
    bvy.append(randint(1, 5) * (-1) ** randint(1, 2))
    br.append(randint(15, 100))
    ballcolor.append(COLORS[randint(0, 5)])


def move_ball(k, dt):
    global bx, by
    circle(screen, ballcolor[k], (bx[k], by[k]), br[k])
    bx[k] += dt * bvx[k]
    by[k] += dt * bvy[k]


def click(clickvent):
    global miss
    p = False
    t = -1
    for i in range(ballcounter):
        if ((clickvent.pos[0] - bx[i]) ** 2 + (clickvent.pos[1] - by[i]) ** 2) <= (br[i] ** 2):
            p = True
            t = i

    if not p: miss += 1  # miss - counter of misses
    return p, t


def sgn(q):
    if q > 0:
        return 1
    elif q < 0:
        return -1
    else:
        return 0


def bounce(k):
    if bx[i] < 0:
        bvx[k] = -1 * sgn(bvx[k]) * randint(1, 5)
        # bvy[k] = randint(1, 5) * (-1) ** randint(1, 2)
        bx[i] = 0
    elif by[i] < 0:
        bvy[k] = -1 * sgn(bvy[k]) * randint(1, 5)
        # bvx[k] = randint(1, 5) * (-1) ** randint(1, 2)
        by[i] = 0
    elif bx[i] > width:
        bvx[k] = -1 * sgn(bvx[k]) * randint(1, 5)
        # bvy[k] = randint(1, 5) * (-1) ** randint(1, 2)
        bx[i] = width
    elif by[i] > height:
        bvy[k] = -1 * sgn(bvy[k]) * randint(1, 5)
        # bvx[k] = randint(1, 5) * (-1) ** randint(1, 2)
        by[i] = height


def counter(action):
    global n
    if action:
        n += 1


misses = []
for i in range(4):
    misses.append(pygame.Surface((250, 100)))

for i in range(4):
    line(misses[i], (255, 255, 255), (25, 25), (75, 75), 7)
    line(misses[i], (255, 255, 255), (25, 75), (75, 25), 7)
    line(misses[i], (255, 255, 255), (100, 25), (150, 75), 7)
    line(misses[i], (255, 255, 255), (100, 75), (150, 25), 7)
    line(misses[i], (255, 255, 255), (175, 25), (225, 75), 7)
    line(misses[i], (255, 255, 255), (175, 75), (225, 25), 7)

line(misses[1], (255, 0, 0), (25, 25), (75, 75), 5)
line(misses[1], (255, 0, 0), (25, 75), (75, 25), 5)
line(misses[2], (255, 0, 0), (25, 25), (75, 75), 5)
line(misses[2], (255, 0, 0), (25, 75), (75, 25), 5)
line(misses[3], (255, 0, 0), (25, 25), (75, 75), 5)
line(misses[3], (255, 0, 0), (25, 75), (75, 25), 5)
line(misses[2], (255, 0, 0), (100, 25), (150, 75), 5)
line(misses[2], (255, 0, 0), (100, 75), (150, 25), 5)
line(misses[3], (255, 0, 0), (100, 25), (150, 75), 5)
line(misses[3], (255, 0, 0), (100, 75), (150, 25), 5)
line(misses[3], (255, 0, 0), (175, 25), (225, 75), 5)
line(misses[3], (255, 0, 0), (175, 75), (225, 25), 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
miss = 0
action = False
gameover = False
ballcounter = 0
maxballs = n
newb = True
anotherball = 31
pygame.time.set_timer(anotherball, 4000)

while not finished:

    if not gameover:
        textsurface = myfont.render('SCORE:' + str(n), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))
        screen.blit(misses[miss], (0, 100))
        if newb:
            new_ball()
            ballcounter += 1
        for i in range(ballcounter):
            bounce(i)
            move_ball(i, 2)
        pygame.display.update()
        newb = False
    else:
        textsurface1 = myfont.render('GAME OVER! YOUR SCORE:' + str(n), False, (255, 255, 255))
        screen.blit(textsurface1, (0, 0))
        pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == anotherball:
            newb = True
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            r, u = click(event)
            counter(r)
            if r:
                bx.pop(u)
                by.pop(u)
                bvx.pop(u)
                bvy.pop(u)
                br.pop(u)
                ballcolor.pop(u)
                ballcounter -= 1
                # newb = True

        if miss >= 3:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True

    screen.fill(BLACK)
pygame.quit()
