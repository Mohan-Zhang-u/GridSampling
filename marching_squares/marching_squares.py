import numpy as np
import cv2
from metaball import MetaBall
from lookup_table import LUT


WIDTH = 608
HEIGHT = 416
BLOCK_SIZE = 8
HALF_SIZE = BLOCK_SIZE / 2.0

VIS_EACH_BALL = True
VIS_BLOCK = True
VIS_MARCHSQUARE = True
MARCHSQUARE_LINEAR_INTERP = True


class Block:
    def __init__(self):
        x = np.linspace(HALF_SIZE, WIDTH - HALF_SIZE, WIDTH / BLOCK_SIZE)
        y = np.linspace(HALF_SIZE, HEIGHT - HALF_SIZE, HEIGHT / BLOCK_SIZE)
        self.xs, self.ys = np.meshgrid(x, y)

    def draw(self, img, obj):
        values = obj.eval(self.xs, self.ys)
        inds_x, inds_y = np.where(values >= 0)
        for ind_x, ind_y in zip(inds_x, inds_y):
            xx = self.xs[ind_x, ind_y]
            yy = self.ys[ind_x, ind_y]
            x0, x1 = int(xx - HALF_SIZE), int(xx + HALF_SIZE)
            y0, y1 = int(yy - HALF_SIZE), int(yy + HALF_SIZE)
            img[y0:y1, x0:x1, 0] = 255


class MarchSquare:
    def __init__(self):
        # block center coordinates
        x = np.linspace(HALF_SIZE, WIDTH - HALF_SIZE, WIDTH / BLOCK_SIZE)
        y = np.linspace(HALF_SIZE, HEIGHT - HALF_SIZE, HEIGHT / BLOCK_SIZE)
        self.xs, self.ys = np.meshgrid(x, y)
        # block vertex coordinates
        x = np.linspace(0, WIDTH, WIDTH / BLOCK_SIZE + 1)
        y = np.linspace(0, HEIGHT, HEIGHT / BLOCK_SIZE + 1)
        self.xx, self.yy = np.meshgrid(x, y)
        # look up tabel
        self.lut = LUT()

    def draw(self, img, obj, linear_interp=False):
        values = obj.eval(self.xx, self.yy)
        value_0 = values[1:, :-1]  # bottom-left
        value_1 = values[1:, 1:]  # bottom-right
        value_2 = values[:-1, 1:]  # top-right
        value_3 = values[:-1, :-1]  # top-left
        index = (value_3 >= 0).astype(np.int32) * 8 + \
                (value_2 >= 0).astype(np.int32) * 4 + \
                (value_1 >= 0).astype(np.int32) * 2 + \
                (value_0 >= 0).astype(np.int32)
        values = np.concatenate((value_0[:, :, np.newaxis],
                                 value_1[:, :, np.newaxis],
                                 value_2[:, :, np.newaxis],
                                 value_3[:, :, np.newaxis]), 2)
        inds_x, inds_y = np.where(index > 0)
        for ind_x, ind_y in zip(inds_x, inds_y):
            xc = self.xs[ind_x, ind_y]
            yc = self.ys[ind_x, ind_y]
            id = index[ind_x, ind_y]
            value = values[ind_x, ind_y, :]
            draw_func = self.lut.lookup(id, value, linear_interp)
            draw_func(img, xc, yc, HALF_SIZE)


block = Block()
march_square = MarchSquare()

object = MetaBall(WIDTH, HEIGHT)

for i in range(1000):
    if VIS_BLOCK:
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        block.draw(img, object)
        if VIS_EACH_BALL:
            object.draw(img)
        cv2.imshow('MetaBall by Blocks', img)

    if VIS_MARCHSQUARE:
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        march_square.draw(img, object, False)
        if VIS_EACH_BALL:
            object.draw(img)
        cv2.imshow('MetaBall by Marching Squares', img)

    if MARCHSQUARE_LINEAR_INTERP:
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        march_square.draw(img, object, True)
        if VIS_EACH_BALL:
            object.draw(img)
        cv2.imshow('MetaBall by Linear-Interpolated Marching Squares', img)

    key = cv2.waitKey(100)
    if key == 32:  # space to pause
        cv2.waitKey()  # any key to resume
    object.step()
