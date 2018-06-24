import math

from matplotlib import pyplot as plt

from iterative_fractal_generator import Point, Fragment, fractaliter

KOCH_HEIGHT = math.sqrt((1.0/3)**2 - (1.0/6)**2)
KOCH_CURVE = [Point(0,0), Point(1.0/3, 0), Point(0.5, KOCH_HEIGHT), Point(2.0/3,0), Point(1,0)]

y = math.sqrt(6*6 + 3*3)

frag1 = Fragment( [Point(6, 0), Point(0, 0)], unit_fragment=KOCH_CURVE)
frag2 = Fragment( [Point(0, 0), Point(3, y)], unit_fragment=KOCH_CURVE)
frag3 = Fragment( [Point(3, y), Point(6, 0)], unit_fragment=KOCH_CURVE)

fractaliter(frag1, 7, plot_all_iterations=False)
fractaliter(frag2, 7, plot_all_iterations=False)
fractaliter(frag3, 7, plot_all_iterations=False)
plt.show()
