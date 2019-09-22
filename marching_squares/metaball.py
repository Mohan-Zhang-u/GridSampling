import numpy as np
import random as rnd
import cv2


NUM_BALL = 6
RADIUS_MIN = 20
RADIUS_MAX = 60
SPEED_MIN = 1
SPEED_MAX = 10


class MetaBall:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_ball = NUM_BALL
        self.balls = []
        for i in range(self.num_ball):
            self.balls.append(Ball(width, height))

    def step(self):
        for ball in self.balls:
            ball.step()

    def eval(self, x, y):
        value = 0
        for ball in self.balls:
            value += ball.eval(x, y)
        return value - 1

    def draw(self, img):
        for ball in self.balls:
            ball.draw(img)


class Ball:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        rnd.seed(seed)
        self.x = rnd.randint(0, self.width - 1)
        self.y = rnd.randint(0, self.height - 1)
        self.radius = rnd.randint(RADIUS_MIN, RADIUS_MAX)

        self.vx = (rnd.random() * (SPEED_MAX - SPEED_MIN) + SPEED_MIN) * np.sign(rnd.random())
        self.vy = (rnd.random() * (SPEED_MAX - SPEED_MIN) + SPEED_MIN) * np.sign(rnd.random())

    def step(self):
        """ the ball bounces back when hits the boundary """
        self.x += self.vx
        if self.x >= (self.width - 1 - self.radius):
            self.x = self.width - 1 - self.radius
            self.vx *= -1
        elif self.x <= self.radius:
            self.x = self.radius
            self.vx *= -1

        self.y += self.vy
        if self.y >= (self.height - 1 - self.radius):
            self.y = self.height - 1 - self.radius
            self.vy *= -1
        elif self.y <= self.radius:
            self.y = self.radius
            self.vy *= -1

    def eval(self, x, y):
        return self.radius ** 2 / ((x - self.x) ** 2 + (y - self.y) ** 2 + 1e-9)

    def draw(self, img):
        cv2.circle(img, (int(self.x), int(self.y)), self.radius, [0, 0, 255], 1)


if __name__ == '__main__':
    WIDTH = 608
    HEIGHT = 416
    metaball = MetaBall(WIDTH, HEIGHT)

    for i in range(100):
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        metaball.draw(img)
        cv2.imshow('MetaBall', img)
        cv2.waitKey(100)
        metaball.step()