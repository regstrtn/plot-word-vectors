from __future__ import print_function
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import spline


def readvectors(filename):
    f = open(filename, "r")
    d = {}
    f.readline()
    for line in f:
        l = line.split()
        numbers = [float(x) for x in l[1:]]
        a = np.array(numbers)
        d[l[0]] = a
    print(d.keys())
    T = d['sweat']    
    #for i in range(10):
    # l = f.readline()
    #v = l.split()
    #v = v[1:]
    #numbers = [ float(x) for x in v ]
    #a = np.array(numbers).reshape((200,1))
    #print(a)
    xnew = np.linspace(a.min(), a.max(),300)
    #power_smooth = spline(T,power,xnew)
    #plt.plot(power_smooth)
    plt.plot(a,'bo-',markevery=10)
    plt.show()

readvectors("vectors.txt")
