from utils import *
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

a = function_coverter(lambda x, y: x ** 2 + y ** 2, "<", 1)
b = function_coverter(lambda x, y: x, ">", 0)
c = function_coverter(lambda x, y: y, ">", 0)
d = function_coverter(lambda x, y: np.sin(x), "<", 0)
e = function_coverter(lambda x, y: x ** 2 + (y - np.e**((1/3) * np.log(x**2))) ** 2, "<", 1) # heart shape
f = function_coverter(lambda x, y: x + y, "<", 1)
g = function_coverter(lambda x, y: x**2/3 + y**2/5, "<", 1)
h = function_coverter(lambda x, y: (1 + 0.9 * np.cos(8 * x)) * (1 + 0.1 * np.cos(24 * x)) * (0.9 + 0.05 * np.cos(200 * x)) * (1 + np.sin(x)) + y, "<", np.pi)
i = function_coverter(lambda x, y: (1 + 0.9 * np.cos(8 * x)) * (1 + 0.1 * np.cos(24 * x)) * (0.9 + 0.05 * np.cos(200 * x)) * (1 + np.sin(x)) - y, "<", np.pi)
j = function_coverter(lambda x, y: np.sin(x+y) - np.cos (x*y), "<", 1)


functions = \
    [
        function_coverter(lambda x, y: x ** 2 + y ** 2, "<", 1),
        function_coverter(lambda x, y: x, ">", 0),
        function_coverter(lambda x, y: y, ">", 0),
        function_coverter(lambda x, y: np.sin(x), "<", 0),
        function_coverter(lambda x, y: x ** 2 + (y - np.e**((1/3) * np.log(x**2))) ** 2, "<", 1) # x ** 2 + (y - x ** (2 / 3)) ** 2 < 1)
        # here if we use x ** (2 / 3), it might create complex number, so we convert it to e^ln
    ]

functions = [a]
functions = [e]
functions = [b,c,f]
functions = [g]
functions = [h]
functions = [j]
# functions = [b,c,e]

grid_density_x = grid_density_y = 0.05 #0.01
origin_x = origin_y = 0
stopping_x = stopping_y = 10
bisection_interval = (grid_density_x + grid_density_y) / 2 / 50   #/100


intersection_points = []
edge_lines = []
marching_square(origin_x, origin_y, stopping_x, stopping_y, grid_density_x, grid_density_y,
                    functions, bisection_interval, intersection_points, edge_lines)

lc = LineCollection(edge_lines) #, linewidths=2
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
plt.show()
# ax.margins(0.1)

