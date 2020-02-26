from integrating_function.integrating_function import integrate_points
import matplotlib.pyplot as plt
import numpy as np
import random
import time
#Function to get time in milliseconds like millis in Arduino
millis = lambda : time.time_ns() // 1000000

#Function semi-stolen from stackoverflow to generate a pseudo random curve
#https://stackoverflow.com/questions/29050164/produce-random-wavefunction
X = np.linspace(1, 1000,1000)
def f(x,N=10):
    #Return an array of values that simulates the curve/signal
    y = 0;result = []
    for _ in x:
        result.append(y)
        y += np.random.normal(scale=1)
    x = np.array(result)
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

signal = f(X)
#Simulate a random curve and aply the double integration
if(__name__=='__main__'):
    pila = [] #The storage for the recived curve values
    sums = [] #The acumulative values of the integral over time
    sum = 0
    times = []#Record time for each curve´s input

    ############################ Signal/Curve over time ############################
    plt.ion()
    for (s_ix,s) in enumerate(signal):
        pila.append([millis(),s])
        if(len(pila)>=4): #Get the last 4 values of the curve´s recived data
            pila = pila[-4:]
            #Add the area of the current curve section to the rest of the area(the last)
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
