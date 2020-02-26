import matplotlib.pyplot as plt
curve = [[1,1],[2,2],[3,3],[4,2],[5,1],[6,0],[7,-1],[8,-2]]
#Si se trata de una señal, el primer valor de los puntos puede ser el tiempo de
#la señal medido, el segundo el valor como tal. Se puede hacer una lista que acumule
#cierto rango de  valores (4) de la señal y que se renoven en tiempo real.

#Si por ejemplo la señal es de velocidad, la primera integral es el desplazamiento
#, si la señal fuera aceleración la primera integral sería velocidad, y la segunda,
#el desplazamiento, si se asume que la ubicación inicial es en el origen 0, además,
#de desplazamiento es la posición

def integrate_points(points):
    """Format of points  = [[x,y],[],[]..] , return the list of points of
    acumulative graph of an integral though x"""
    sums = []
    last_p = points[0]
    sum = 0
    for px ,p in enumerate(points):
        #local_area = (pY + last_pY)(pX-last_pX)/2
        local_area = (p[1] + last_p[1])*(p[0]-last_p[0])/2
        last_p = p
        sum+=local_area
        sums.append([px,sum])
    return sums

if(__name__ == '__main__'):
    pila = []
    first_integral = integrate_points(curve)
    second_integral = integrate_points(first_integral)
    print(first_integral[-1][1],second_integral[-1][1])
    pass
