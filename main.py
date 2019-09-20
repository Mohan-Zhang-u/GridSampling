from utils import *

functions = \
    [
        function_coverter(lambda x, y: x ** 2 + y ** 2, "<", 1),
        function_coverter(lambda x, y: x, ">", 0),
        function_coverter(lambda x, y: y, ">", 0),
        function_coverter(lambda x, y: np.sin(x), "<", 0),
        function_coverter(lambda x, y: x ** 2 + (y - x ** (2 / 3)) ** 2, "<", 1)
    ]

grid_density_x = grid_density_y = 0.001
origin_x = origin_y = 0
stopping_x = stopping_y = 10
bisection_interval = (grid_density_x + grid_density_y) / 2 / 1000



