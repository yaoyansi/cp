""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# PredatorPrey.py: Variations on the Lotka - Volterra model
from visual import *
from visual.graph import *

Tmin = 0.0
Tmax = 500.0                                                  # endpoints
y = zeros( (2), float)
Ntimes = 1000
y[0] = 2.0
y[1] = 1.3                                                   # initialize
h = (Tmax - Tmin)/Ntimes 
t = Tmin

def f( t, y, F):   # FUNCTION of your choice here
        F[0] = 0.2*y[0]*(1 - (y[0]/(20.0) )) - 0.1*y[0]*y[1] # RHS 1st eq
        F[1]  = - 0.1*y[1] + 0.1*y[0]*y[1];                  # RHS 2nd eq
		 
def rk4(t, y, h, Neqs):  # rk4 method, *DO NOT MODIFY*, instead, modify f
    F = zeros((Neqs), float)
    ydumb = zeros((Neqs), float)
    k1    = zeros((Neqs), float)
    k2    = zeros((Neqs), float)
    k3    = zeros((Neqs), float)
    k4    = zeros((Neqs), float)
    f(t, y, F)
    for i in range(0, Neqs):
        k1[i] = h*F[i]
        ydumb[i] = y[i] + k1[i]/2.
    f(t + h/2., ydumb, F)
    for i in range(0, Neqs):
        k2[i] = h*F[i]
        ydumb[i] = y[i] + k2[i]/2.
    f(t + h/2., ydumb, F)
    for i in range(0, Neqs):
        k3[i] =  h*F[i]
        ydumb[i] = y[i] + k3[i]
    f(t + h, ydumb, F)
    for i in range(0, Neqs):
        k4[i] = h*F[i]
        y[i] = y[i] + (k1[i] + 2.*(k2[i] + k3[i]) + k4[i])/6.
				
# == == == == == == == = == == == == = rk4 ends == == == == == == ==
        
graph1 = gdisplay(x= 0,y= 0, width = 500, height = 400, 
                  title = 'Prey p(green) and predator P(yellow) vs time',
           xtitle = 't', ytitle = 'P, p',xmin=0,xmax=500,ymin=0,ymax=3.5)
funct1 = gcurve(color = color.yellow)
funct2 = gcurve(color = color.green)
graph2 = gdisplay(x= 0,y= 400, width = 500, height = 400,
                  title = 'Predator P vs prey p',
              xtitle = 'P', ytitle = 'p',xmin=0,xmax=2.5,ymin=0,ymax=3.5)
funct3 = gcurve(color = color.red)

for t in arange(Tmin, Tmax + 1, h):
    funct1.plot(pos = (t, y[0]) )
    funct2.plot(pos = (t, y[1]) )
    funct3.plot(pos = (y[0], y[1]) )
    rate(60)
    rk4(t, y, h, 2)
