""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Grade.py: Using Matplotlib's plot command with multi data sets & curves

import pylab as p                                            # Matplotlib
from numpy import*

p.title('Grade Inflation')                             # Title and labels
p.xlabel('Years in College')
p.ylabel('GPA')

xa = array([-1, 5])                                 # For horizontal line
ya = array([0, 0])                                       # Array of zeros
p.plot(xa, ya)                                     # Draw horizontal line
                                                   
x0 = array([0, 1, 2, 3, 4])                           # Data set 0 points
y0 = array([-1.4, +1.1, 2.2, 3.3, 4.0])
p.plot(x0, y0, 'bo')                          # Data set 0 = blue circles
p.plot(x0, y0, 'g')                                   # Data set 0 = line

y1 = array([4.0, 2.7, -1.8, -0.9, 2.6])               # Data set 1 points
t = arange(0, 5, 1)
p.plot(t, y1, 'r')                                          

err1sup = array([1.0, 0.3, 1.2, 0.4, 0.1])        # Asymmetric error bars
err1inf = array([2.0, 0.6, 2.3, 1.8, 0.4])                    
p.errorbar(t, y1, [err1inf, err1sup], fmt = 'o')        # Plot error bars

p.grid(True)                                                  # Grid line
p.show()                                          # Create plot on screen
