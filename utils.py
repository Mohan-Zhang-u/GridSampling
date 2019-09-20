import numpy as np


def function_coverter(lambda_function, constraint_direction, constant):
    """
    something like function_coverter(lambda x, y:np.sin(x)+ y**2 , "<", 3) evaluates sin(x)+y^2-3<3
    :param lambda_function: a function takes x and y, returns a scalar result
    :param constraint_direction:
    :param constant:
    :return:
    """
    if constraint_direction in ["eq", "equal", "="]:
        return lambda x, y: abs(lambda_function(x, y) - constant)
    elif constraint_direction in [">=", "geq", ">", "gt"]:
        return lambda x, y: lambda_function(x, y) - constant
    elif constraint_direction in ["<=", "leq", "<", "lt"]:
        return lambda x, y: constant - lambda_function(x, y)


def constraint_satisfaction(functions, point):
    """
    2-D functions should be a list of constraints which takes two arguments, x and y.
    given x and y, the constraint should return a positive value if (x,y) satisfies the constraint (in the shape),
    negative if (x,y) breaks the constraint (out of the shape), and 0 if on the boundary of that function
    :param functions: [functions]
    :param point: (int, int)
    :return: (number, [results]): the min value of the evaluation results, and the list of evaluation results.
    """
    evaluations = [i(point[0], point[1]) for i in functions]
    return min(evaluations), evaluations


def bisection_2d(functions, start, end, bisection_interval):
    """
    start * end <=0, but at most one of start or end == 0.

    """
    if constraint_satisfaction(functions, start)[0] == 0:
        return start
    elif constraint_satisfaction(functions, end)[0] == 0:
        return end
    else:
        n_start = np.array(start)
        n_end = np.array(end)
        if np.linalg.norm(n_start - n_end) < bisection_interval:
            if np.random.randint(0, 2):
                return start
            else:
                return end
        else:
            if constraint_satisfaction(functions, start)[0] * \
                    constraint_satisfaction(functions, tuple((n_start + n_end) / 2))[0] <= 0:
                return bisection_2d(functions, start, tuple((n_start + n_end) / 2), bisection_interval)
            else:
                return bisection_2d(functions, tuple((n_start + n_end) / 2), end, bisection_interval)


# def determ_patern(vertices_coordinate, vertices_result, intersection_points, edge_lines):
#     """
#
#     :param vertices_coordinate: ((0,0), (0,1), (1,0), (1,1))
#     :param vertices_result: (float, float, float, float)
#     :param intersection_points:
#     :param edge_lines:
#     :return:
#     """
#     if


a = function_coverter(lambda x, y: x ** 2 + y ** 2, "<", 1)
b = function_coverter(lambda x, y: x, ">", 0)
c = function_coverter(lambda x, y: y, ">", 0)
d = function_coverter(lambda x, y: np.sin(x), "<", 0)
e = function_coverter(lambda x, y: x ** 2 + (y - x ** (2 / 3)) ** 2, "<", 1)  # heart shape

# import sympy
# x, y = sympy.symbols('x y')
# p1 = sympy.plot_implicit(sympy.Eq(x ** 2 + (y - x ** (2 / 3)) ** 2, 1), show=False)
# p2 = sympy.plot_implicit(sympy.Eq(x ** 2 + y ** 2, 1), show=False)
# p1.extend(p2)
# p1.show()

# import matplotlib.pyplot as plt
# from matplotlib.collections import LineCollection
# # lines = [((0, 1), (1, 1)), ((2, 2), (3, 3)), ((1.1, 2.222)), ((5.01, 5.02))]
# # lines = np.array([[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)], [(1.1, 2.222)], [(5.01, 5.02)]])
# lines = [[(5, 5), (5.01,5)], [(5.02, 6.02),(5.03, 6.02)]]
# lc = LineCollection(lines) #, linewidths=2
# fig, ax = plt.subplots()
# ax.add_collection(lc)
# ax.autoscale()
# plt.show()
# # ax.margins(0.1)


# ----------- debugging --------------
# print(constraint_satisfaction([a], (0,0))[0])
# print(bisection_2d([a], (0, -0.5), (0, 10), 0.0001))
