from integrating_function.integrating_function import integrate_points
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from math import sqrt
#Function to get time in milliseconds like millis in Arduino
millis = lambda : time.time_ns() // 1000000

#Function semi-stolen from stackoverflow to generate a pseudo random signal
#https://stackoverflow.com/questions/29050164/produce-random-wavefunction
X = np.linspace(1, 1000,1000)
def f(x,N=10):
    y = 0;result = []
    for _ in x:
        result.append(y)
        y += np.random.normal(scale=1)
    x = np.array(result)
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

'''def f(x):
    return [sqrt(x) for x in range(0,100)]'''

signal = f(X)
#Simulate a random signal and aply the double integration
if(__name__=='__main__'):
    pila = [] #The storage for the recived signal values
    sums = [] #The acumulative values of the integral thorugh time
    sum = 0
    times = []#Record time for each signal input

    ############################Signal through time############################
    plt.ion()
    for (s_ix,s) in enumerate(signal):
        pila.append([millis(),s])
        if(len(pila)>=4): #Get the last 4 values of the signal
            pila = pila[-4:]
            #Add the area of the current signal section to the rest of the area(the last)
            sum += integrate_points(integrate_points(pila))[-1][-1]
            sums.append(sum)
            times.append(millis())
        #Current second integral is sums[-1]
        #plot
        plt.subplot(2,1,1)
        plt.plot(signal[:s_ix])
        plt.ylabel('Signal')
        plt.subplot(2,1,2)
        plt.plot(times,sums)
        plt.ylabel('Second integral respect of time')
        plt.xlabel('Time(milliseconds)')
        plt.draw()
        plt.pause(1/(10**100))
    time.sleep(10)
    pass
