""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# EasyVisual.py: Simple graph object using Visual

from visual.graph import *                                    # Import Visual

graph1 = gdisplay(width=500,height=300)
Plot1 =  gcurve(color=color.white)                            # gcurve method
graph2 = gdisplay(x=500,width=600,height=450, title="Visual plot", xtitle='x',
        ytitle='f(x)', foreground=color.black, background=color.white)
Plot2 = gdots(color=color.green)

for x in arange(0,8.1,0.1):     Plot1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x)))         

Plot2 = gdots(color=color.green)

for x in arange(-5,5.0,0.1):    Plot2.plot(pos=(x,cos(x)))
