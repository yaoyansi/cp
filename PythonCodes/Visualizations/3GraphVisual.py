""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""                       
  
# 3GraphVisual.py: 3 plots in the same figure, with bars, dots and curve

from visual import *
from visual.graph import*  

string = "yellow: sin^2(x), white: cos^2(x)/3, red: sin(x)*cos(x)"
graph1 = gdisplay(title=string, xtitle='x', ytitle='y')

y1 = gcurve(color=color.yellow, delta=3)                       # Curve
y2 = gvbars(color=color.white)                         # Vertical bars
y3 = gdots(color=color.red, delta=3)                            # Dots
   
for x in arange(-5, 5, 0.1):                       # arange for floats
    y1.plot( pos=(x, sin(x)*sin(x)) )
    y2.plot( pos=(x, cos(x)*cos(x)/3.) )
    y3.plot( pos=(x, sin(x)*cos(x)) )
