import numpy; import mayavi
from mayavi.mlab import *

n_mer, n_long = 6, 11 ; pi =numpy.pi 
dphi  =  pi / 1000.0
phi = numpy.arange(0.0, 2 * pi + 0.5 * dphi, dphi)
mu = phi * n_mer
x = numpy.cos(mu) * (1 + numpy.cos(n_long * mu / n_mer) * 0.5)
y = numpy.sin(mu) * (1 + numpy.cos(n_long * mu / n_mer) * 0.5)
z = numpy.sin(n_long * mu / n_mer) * 0.5

plot3d(x, y, z, numpy.sin(mu), tube_radius=0.025, colormap='Spectral')
mayavi.mlab.show()