""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""                                    

# EasyPlot.py Simple plot using matplotlib

from pylab import *                                       # For matplotlib

Xmin = -5.0                                                       
Xmax = 5.0                                                       
Npoints = 500
xincrement = (Xmax-Xmin)/Npoints                              
x = arange(Xmin, Xmax, xincrement)                         # x range 
y = (sin(x))**2                                            # Function plotted
print("plotting")                                             
plot(x, y, '-', lw=2)                
xlabel('x')                            
text(0.5,-0.1,'x axis divided in 500 intervals')
ylabel('f(x)')
title('f(x) vs x')
grid(True)                                           # Produce lines for grid
show()               