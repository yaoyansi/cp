""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Simple3Dplot.py: Simple matplotlib 3D plot; rotate & scale via mouse
			
import matplotlib.pylab  as p                                     
from mpl_toolkits.mplot3d import Axes3D 
#from visual import *    # for range
import numpy
from mayavi.mlab import *

print("Please be patient, I have packages to import & points to plot")
delta = 0.1
x = p.arange( -3., 3., delta )
y = p.arange( -3., 3., delta )
X, Y = p.meshgrid(x, y)
Z = p.sin(X)*p.cos(Y)
p.mesh(X, Y, Z, colormap='YlGnBu')
# surface height
s = surf(X, Y, Z) 
fig = p.figure()                                          # create figure
ax = Axes3D(fig)                                             # plots axes
ax.plot_surface(X, Y, Z)                                      # surface
ax.plot_wireframe(X, Y, Z, color = 'r')                       # wireframe
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

p.show()                                                    # show figure
