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


def marching_square(origin_x, origin_y, stopping_x, stopping_y, grid_density_x, grid_density_y, intersection_points,
                    edge_lines):
    x = origin_x - stopping_x
    y = origin_y - stopping_y
    while x < origin_x + stopping_x:
        while y < origin_y + stopping_y:
            bot_left = (x, y)
            bot_right = (x + grid_density_x, y)
            top_left = (x, y + grid_density_y)
            top_right = (x + grid_density_x, y + grid_density_y)
            vertices_result = [constraint_satisfaction(functions, bot_left[0], bot_left[1]),
                               constraint_satisfaction(functions, bot_right[0], bot_right[1]),
                               constraint_satisfaction(functions, top_left[0], top_left[1]),
                               constraint_satisfaction(functions, top_right[0], top_right[1])]
            determ_patern((bot_left, bot_right, top_left, top_right), vertices_result, intersection_points, edge_lines)

            y += grid_density_y
        x += grid_density_x

