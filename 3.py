import numpy as np
import matplotlib as pylab

def funkcja1(x):
   return (np.exp(5*x)/100)-(1/4)
   
def funkcja11P(x, delta):
    return (funkcja1(x+(delta/2))-(x-(delta/2)))/delta

def zadanie3(a):
    x = a
    for k in range(20000):
        if np.abs(funkcja1(x)) < 0.001:
            return print("Dla punktu poczatkowego ",a,", pierwiastek równy ",x," znaleziony w ", k," iteracji.")
        else: 
            x = x-(funkcja1(x)/funkcja11P(x, 0.001))
    print("Przekroczono zakres iteracji")

print("Zadanie 3")
zadanie3(0.1)
zadanie3(0.9)