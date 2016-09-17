""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# DWT.py:  Discrete Wavelet Transform, Daubechies type, global variables
from visual import * 
from visual.graph import *

sq3 = sqrt(3);           fsq2 = 4.0*sqrt(2);      N = 1024     # N = 2^n
c0 = (1+sq3)/fsq2;            c1 = (3+sq3)/fsq2      # Daubechies 4 coeff
c2 = (3-sq3)/fsq2;             c3 = (1-sq3)/fsq2
transfgr1 = None          # indicate that displays have not been made yet
transfgr1 = None

def chirp( xi):                                            # chirp signal
    y = sin(60.0*xi**2);
    return y;

def daube4(f, n, sign):           # DWT if sign >= 0, inverse if sign < 0
    global transfgr1, transfgr2
    tr = zeros( (n + 1), float)                      # temporary variable
    if n < 4 : return
    mp = n/2                                          # midpoint of array
    mp1 = mp + 1                                      # midpoint plus one
    if sign >= 0:                                                   # DWT
        j = 1
        i = 1
        maxx  = n/2
        if n > 128:                                   # appropiate scales
            maxy = 3.0
            miny = - 3.0
            Maxy = 0.2
            Miny = - 0.2
            speed = 50                                        # fast rate
        else:
            maxy = 10.0
            miny = - 5.0
            Maxy = 7.5
            Miny = - 7.5
            speed = 8                                    # for lower rate
        if transfgr1:
            transfgr1.display.visible = False
            transfgr2.display.visible = False
            del transfgr1
            del transfgr2
        transfgr1 = gdisplay(x=0, y=0, width=600, height=400,\
				          title='Wavelet TF, down sample + low pass', xmax=maxx,\
				                     xmin=0, ymax=maxy, ymin=miny)
        transf  = gvbars(delta=2.*n/N,color=color.cyan,display=transfgr1)     
        transfgr2 = gdisplay(x=0, y=400, width=600, height=400,\
				                   title='Wavelet TF, down sample + high pass',\
														 xmax=2*maxx, xmin=0, ymax=Maxy, ymin=Miny)
        transf2 = gvbars(delta=2.*n/N,color=color.cyan,display=transfgr2)
        while j <= n - 3:
            rate(speed)
            tr[i] = c0*f[j] + c1*f[j+1] + c2*f[j+2] + c3*f[j+3]# low-pass
            transf.plot(pos = (i, tr[i]) )               # c coefficients
            tr[i+mp] = c3*f[j] - c2*f[j+1] + c1*f[j+2] - c0*f[j+3] # high
            transf2.plot(pos = (i + mp, tr[i + mp]) )
            i += 1                                        # d coefficents
            j += 2                                         # downsampling
        tr[i] = c0*f[n-1] + c1*f[n] + c2*f[1] + c3*f[2]        # low-pass
        transf.plot(pos = (i, tr[i]) )                   # c coefficients
        tr[i+mp] = c3*f[n-1] - c2*f[n] + c1*f[1] - c0*f[2]    # high-pass
        transf2.plot(pos = (i+mp, tr[i+mp]) )
    else:                                                   # inverse DWT
        tr[1] = c2*f[mp] + c1*f[n] + c0*f[1] + c3*f[mp1]       # low-pass
        tr[2] = c3*f[mp] - c0*f[n] + c1*f[1] - c2*f[mp1]      # high-pass
        j = 3
        for i in range (1, mp):
           tr[j] = c2*f[i] + c1*f[i+mp] + c0*f[i+1] + c3*f[i+mp1]   # low
           j += 1                                              # upsample
           tr[j] = c3*f[i] - c0*f[i+mp] + c1*f[i+1] - c2*f[i+mp1]  # high
           j += 1;                                           # upsampling
    for i in range(1, n+1):
        f[i] = tr[i]                                   # copy TF to array

def pyram(f, n, sign):                            # DWT, replaces f by TF
    if (n < 4): return                                     # too few data
    nend = 4                                     # indicates when to stop
    if sign >= 0 :                                            # Transform
        nd = n
        while nd >= nend:                          # Downsample filtering
            daube4(f, nd, sign)
            nd //= 2  
    else:                                                    # Inverse TF
        for nd in range (4, n + 1):                          # Upsampling
            daube4(f , nd, sign)
            nd *= 2   
f = zeros( (N + 1), float)                                  # data vector
inxi = 1.0/N                                           # for chirp signal
xi = 0.0
for i in range(1, N + 1):
    f[i] = chirp(xi)                                     # Function to TF
    xi   += inxi;                   
n = N                                                       # must be 2^m
pyram(f, n, 1)                                                       # TF
# pyram(f, n,  - 1)                                          # Inverse TF
