import math

from matplotlib import pyplot as plt
import numpy as np

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


def unit_vector(p1, p2):
    p3 = Point(p2.x - p1.x, p2.y - p1.y)
    magnitude = math.sqrt(p3.x * p3.x + p3.y * p3.y)
    return Point(p3.x/magnitude, p3.y/magnitude)

def unit_vector_perp(p1, p2):
    p3 = Point(-p2.y + p1.y, p2.x - p1.x)
    magnitude = math.sqrt(p3.x * p3.x + p3.y * p3.y)
    return Point(p3.x/magnitude, p3.y/magnitude)


class Fragment(object):
    def __init__(self, points, unit_fragment=None):
        self.points = points
        if unit_fragment is None:
            self.unit_fragment = self.points
        else:
            self.unit_fragment = unit_fragment


    def to_mpl_args(self):
        return [pt.x for pt in self.points], [pt.y for pt in self.points]

    def fractalize(self):
        fragments = []
        for i in range(len(self.points) - 1):
            new_fragment = self.project_onto(self.points[i], self.points[i+1])
            fragments.append(new_fragment)

        return fragments

    
    def project_onto(self, point1, point2):
        # we want to project the fragment from the coord system
        # that has origin on point1(cartesian) and x-vector on the direction point1, point2 (cartesian)
        # back onto the cartesian system to be able to plot it
        
        # the transformation matrix from cartesian to custom coord is
        x_vector = unit_vector(point1, point2)
        y_vector = unit_vector_perp(point1, point2)
        dx = point2.x - point1.x
        dy = point2.y - point1.y
        x_scale = math.sqrt(dx * dx + dy * dy)
        y_scale = x_scale
        rotate_around_origin_matrix = [[x_vector.x, y_vector.x, point1.x],
                  [x_vector.y, y_vector.y, point1.y],
                  [0, 0, 1]]
        scale_matrix = [[x_scale, 0, 0],
                        [0, y_scale, 0],
                        [0, 0, 1]]
        new_points = [Point(*np.matmul(rotate_around_origin_matrix,
            np.matmul(scale_matrix, [pt.x, pt.y, 1]))[:2]) for pt in self.unit_fragment]
        return Fragment(new_points, self.unit_fragment)

def pointlist_to_mpl_args(points):
    return [pt.x for pt in points], [pt.y for pt in points]


def fractaliter(fragment, num_iter, plot_all_iterations=True):
    if num_iter == 0:
        return fragment.to_mpl_args()

    fragments = [fragment]
    
    for i in range(num_iter):
                
        new_fragments = []
        xs = []
        ys = []
        for fragment in fragments:
            children_fragments = fragment.fractalize()
            new_fragments+=children_fragments
            for cf in children_fragments:
                x, y = cf.to_mpl_args()
                xs+=x
                ys+=y

        fragments = new_fragments
        if plot_all_iterations or i == num_iter - 1:
            plt.plot(xs, ys)

    return xs, ys

KOCH_HEIGHT = math.sqrt((1.0/3)**2 - (1.0/6)**2)
        


FRAG1 = Fragment([Point(0,0), Point(1.0/3, 0), Point(1.0/3, 1.0/3),
                  Point(2.0/3, 1.0/3), Point(2.0/3, 0), Point(1,0)])

KOCH_CURVE = Fragment([Point(0,0), Point(1.0/3, 0), Point(0.5, KOCH_HEIGHT), Point(2.0/3,0), Point(1,0)])
print KOCH_HEIGHT

xs, ys = fractaliter(KOCH_CURVE, 6)
plt.show()
#plt.plot(xs, ys)
#plt.show()
#line = [Point(1,1), Point(3,3)]
#frag2 = frag.project_onto(*line)
#plt.plot(*pointlist_to_mpl_args(line))
#plt.plot(*frag.to_mpl_args())
#plt.plot(*frag2.to_mpl_args())
#plt.show()
