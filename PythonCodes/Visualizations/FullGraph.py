""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# FullGraph.py:       2 - D graph with title and labels
from visual import*	 
from visual.graph import *

graph1 = gdisplay(x = 0, y = 0, width = 600, height = 450, 
          title ='f(x) vs. x', xtitle='x label', ytitle='y = f(x)', 
          xmax = 5., xmin = - 5., ymax = 1.2, ymin = - 1.2, 
          foreground = color.black, background = color.white)

funct1 = gcurve(color = color.cyan)

for x in arange( - 5.,  + 5, 0.1):
    funct1.plot(pos = (x, cos(x) )) 
