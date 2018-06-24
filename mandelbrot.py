import itertools

import numpy as np
from matplotlib import pyplot as plt

def mandelbrot(z,c):
    return z*z +c

xvalues = np.linspace(-1.5,1.5,200)
yvalues = np.linspace(-1.5,1.5,200)
max_iter=100

points = list(itertools.product(xvalues,yvalues))
out_pts = []
in_pts = []

for pt in points:
    z = 0
    c = complex(*pt)
    out=False # we assume the point pt is in the Mandelbrot set
    for i in range(max_iter):
        z = mandelbrot(z,c)
        if abs(z)>2:
            out=True
            break

    if out:
        out_pts.append(pt)
    else:
        in_pts.append(pt)

out_pts = np.array(out_pts)
in_pts = np.array(in_pts)

plt.scatter(out_pts[:,0], out_pts[:,1], color="black")
plt.scatter(in_pts[:,0], in_pts[:,1], color="white")
plt.show()



