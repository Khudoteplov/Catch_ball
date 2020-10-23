import pygame
from pygame.draw import *
from random import randint, uniform

pygame.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 100
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
print('What is your name?')
name = input()

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


class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.radius)

    def bounce(self):
        if self.x < 0:
            self.vx = -1 * sgn(self.vx) * randint(1, 5)
            self.x = 0
        elif self.y < 0:
            self.vy = -1 * sgn(self.vy) * randint(1, 5)
            self.y = 0
        elif self.x > width:
            self.vx = -1 * sgn(self.vx) * randint(1, 5)
            self.x = width
        elif self.y > height:
            self.vy = -1 * sgn(self.vy) * randint(1, 5)
            self.y = height


class Square:
    def __init__(self, x, y, vx, vy, a, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = a
        self.color = color

    def move(self, b, dt):
        self.x += int(self.vx * dt)
        self.y += int(self.vy * dt)
        self.vx, self.vy = self.vx * (1 - b**2 * dt**2)**0.5 + b * dt * self.vy, \
                           self.vy * (1 - b**2 * dt**2)**0.5 - b * dt * self.vx

    def bounce(self):
        if self.x < 0:
            self.vx = -1 * sgn(self.vx) * uniform(2.0, 5.0)
            self.x = 0
        elif self.y < 0:
            self.vy = -1 * sgn(self.vy) * uniform(2.0, 5.0)
            self.y = 0
        elif self.x > width:
            self.vx = -1 * sgn(self.vx) * uniform(2.0, 5.0)
            self.x = width
        elif self.y > height:
            self.vy = -1 * sgn(self.vy) * uniform(2.0, 5.0)
            self.y = height

    def draw(self):
        rect(screen, self.color, (self.x - self.a // 2, self.y - self.a // 2, self.a, self.a))


def click(clickvent):
    global miss
    p = False
    t = -1
    for i in balls:
        if ((clickvent.pos[0] - i.x) ** 2 + (clickvent.pos[1] - i.y) ** 2) <= (i.radius ** 2):
            p = True
            t = i
    for j in squares:
        if (-j.a//2 <= (clickvent.pos[0] - j.x) <= j.a//2) and (-j.a//2 <= (clickvent.pos[1] - j.y) <= j.a//2):
            p = True
            t = j
    if not p:
        miss += 1  # miss - counter of misses
    return p, t


def sgn(q):
    if q > 0:
        return 1
    elif q < 0:
        return -1
    else:
        return 0


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
game_over = False
maxballs = n
new_ball = True
new_square = True
anotherball = 31
pygame.time.set_timer(anotherball, 4000)
balls = []
squares = []
rating = open('leaderboard.txt', 'r')
leaderboard = rating.read()
rating.close()

while not finished:

    if not game_over:
        text_surface = myfont.render('SCORE:' + str(n), False, (255, 255, 255))
        screen.blit(text_surface, (0, 0))
        screen.blit(misses[miss], (0, 100))
        if new_ball:
            balls.append(Ball(randint(100, width - 100),
                              randint(100, height - 100),
                              randint(1, 5) * (-1) ** randint(1, 2),
                              randint(1, 5) * (-1) ** randint(1, 2),
                              randint(15, 100),
                              COLORS[randint(0, len(COLORS) - 1)]))

        if new_square:
            squares.append(Square(randint(50, width - 50),
                                  randint(50, height - 50),
                                  uniform(2.0, 6.0) * (-1) ** randint(1, 2),
                                  uniform(2.0, 6.0) * (-1) ** randint(1, 2),
                                  2 * randint(15, 50),
                                  COLORS[randint(0, len(COLORS) - 1)]))
        for square in squares:
            square.bounce()
            square.draw()
            square.move(0.025, 2)

        for ball in balls:
            ball.bounce()
            ball.draw()
            ball.move(2)
        pygame.display.update()
        new_ball, new_square = False, False
    else:
        textsurface1 = myfont.render('GAME OVER! YOUR SCORE:' + str(n), False, (255, 255, 255))
        screen.blit(textsurface1, (0, 0))
        pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == anotherball:
            new_ball = True
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            r, u = click(event)
            counter(r)
            if r and (u in balls):
                balls.remove(u)
            elif r and (u in squares):
                squares.remove(u)
                n += 999
        if miss >= 3:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
    screen.fill(BLACK)
pygame.quit()
p = False
new_rating = open('leaderboard.txt', 'w')
if len(str(leaderboard)) == 0:
    new_rating.write(str(n) + ' ' + name + '\n')
else:
    for line in leaderboard.split('\n'):
        if len(line) > 0:
            if int(line[0:line.find(' '):1]) >= n:
                new_rating.write(line + '\n')
            elif not p:
                new_rating.write(str(n) + ' ' + name + '\n')
                p = True
    if not p:
        new_rating.write(str(n) + ' ' + name + '\n')
        p = True

new_rating.close()