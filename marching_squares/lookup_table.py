import cv2
import numpy as np


class LUT:
    def __init__(self):
        pass

    def lookup(self, id, value, linear_interp=False):
        if id == 0:
            def draw(img, xc, yc, step):
                pass
        elif id == 1:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                x1 = self.interp(value[0], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [x1, 1], step)
        elif id == 2:
            def draw(img, xc, yc, step):
                x0 = self.interp(value[0], value[1]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, 1], [1, y1], step)
        elif id == 3:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [1, y1], step)
        elif id == 4:
            def draw(img, xc, yc, step):
                x0 = self.interp(value[3], value[2]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, -1], [1, y1], step)
        elif id == 5:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                x1 = self.interp(value[3], value[2]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [x1, -1], step)
                x0 = self.interp(value[0], value[1]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, 1], [1, y1], step)
        elif id == 6:
            def draw(img, xc, yc, step):
                x0 = self.interp(value[3], value[2]) if linear_interp else 0
                x1 = self.interp(value[0], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, -1], [x1, 1], step)
        elif id == 7:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                x1 = self.interp(value[3], value[2]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [x1, -1], step)
        elif id == 8:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                x1 = self.interp(value[3], value[2]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [x1, -1], step)
        elif id == 9:
            def draw(img, xc, yc, step):
                x0 = self.interp(value[3], value[2]) if linear_interp else 0
                x1 = self.interp(value[0], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, -1], [x1, 1], step)
        elif id == 10:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                x1 = self.interp(value[0], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [x1, 1], step)
                x0 = self.interp(value[3], value[2]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, -1], [1, y1], step)
        elif id == 11:
            def draw(img, xc, yc, step):
                x0 = self.interp(value[3], value[2]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, -1], [1, y1], step)
        elif id == 12:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [1, y1], step)
        elif id == 13:
            def draw(img, xc, yc, step):
                x0 = self.interp(value[0], value[1]) if linear_interp else 0
                y1 = self.interp(value[2], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [x0, 1], [1, y1], step)
        elif id == 14:
            def draw(img, xc, yc, step):
                y0 = self.interp(value[3], value[0]) if linear_interp else 0
                x1 = self.interp(value[0], value[1]) if linear_interp else 0
                self.line(img, xc, yc, [-1, y0], [x1, 1], step)
        elif id == 15:
            def draw(img, xc, yc, step):
                pass
        else:
            raise ValueError('id {:d} out of range!'.format(id))
        return draw

    def line(self, img, xc, yc, d0, d1, step):
        pt0 = (int(xc + d0[0] * step), int(yc + d0[1] * step))
        pt1 = (int(xc + d1[0] * step), int(yc + d1[1] * step))
        cv2.line(img, pt0, pt1, [0, 255, 0], 1)

    def interp(self, v0, v1):
        return 2.0 * (0 - v0) / (v1 - v0 + 1e-9) - 1


def vis_lut():
    WIDTH = 800
    HEIGHT = 600
    BLOCK_SIZE = 60
    HALF_SIZE = BLOCK_SIZE / 2.0

    # block center coordinates
    x = np.arange(160, WIDTH, 160)
    y = np.arange(120, HEIGHT, 120)
    xs, ys = np.meshgrid(x, y)
    # block vertex coordinates
    x2 = np.zeros(5, np.int64)
    x2[:-1] = x - BLOCK_SIZE / 2
    x2[-1] = x[-1] + BLOCK_SIZE / 2
    y2 = np.zeros(5, np.int64)
    y2[:-1] = y - BLOCK_SIZE / 2
    y2[-1] = y[-1] + BLOCK_SIZE / 2
    xx, yy = np.meshgrid(x2, y2)

    lut = LUT()
    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    for i in range(4):
        for j in range(4):
            xxc = xs[i, j]
            yyc = ys[i, j]

            id = i * 4 + j
            str = '{0:04b}'.format(id)
            value = [int(s) for s in str[::-1]]
            draw_func = lut.lookup(id, value, False)
            draw_func(img, xxc, yyc, HALF_SIZE)

            cv2.rectangle(img, (int(xxc - HALF_SIZE), int(yyc - HALF_SIZE)),
                          (int(xxc + HALF_SIZE), int(yyc + HALF_SIZE)), [255, 255, 255], 1)

            color = [0, 255, 0] if value[0] == 1 else [255, 255, 255]
            cv2.circle(img, (int(xxc - HALF_SIZE), int(yyc + HALF_SIZE)), 4, color, -1)
            color = [0, 255, 0] if value[1] == 1 else [255, 255, 255]
            cv2.circle(img, (int(xxc + HALF_SIZE), int(yyc + HALF_SIZE)), 4, color, -1)
            color = [0, 255, 0] if value[2] == 1 else [255, 255, 255]
            cv2.circle(img, (int(xxc + HALF_SIZE), int(yyc - HALF_SIZE)), 4, color, -1)
            color = [0, 255, 0] if value[3] == 1 else [255, 255, 255]
            cv2.circle(img, (int(xxc - HALF_SIZE), int(yyc - HALF_SIZE)), 4, color, -1)

            cv2.putText(img, '{:s}={:d}'.format(str, id), (xxc - 50, yyc - 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), lineType=cv2.LINE_AA)

    cv2.imshow('Lookup Table', img)
    cv2.waitKey()


if __name__ == '__main__':
    vis_lut()