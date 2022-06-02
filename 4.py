import numpy as np
import matplotlib as pylab

def funkcja1(x):
    return x**5-x+1

def funkcja1p(x, delta):
    return (funkcja1(x+(delta/2))-(x-(delta/2)))/delta

def funkcja2(x):
    return x*(1-x)

def funkcja2p(x, delta):
    return (funkcja2(x+(delta/2))-(x-(delta/2)))/delta

def zadanie4(a):
    x = a
    for k in range(5000):
        if np.abs(funkcja1(x)) < 0.001:
            return print("Dla punktu poczatkowego ",a,", pierwiastek równy ",x," znaleziony w ", k," iteracji.")
        else: 
            x = x-(funkcja1(x)/funkcja1p(x, 0.001))
    print("Przeproczono zakres iteracji")

def zadanie4_1(a):
    x = a
    for k in range(5000):
        if np.abs(funkcja2(x)) < 0.001:
            return print("Dla punktu poczatkowego ",a,", pierwiastek równy ",x," znaleziony w ", k," iteracji.")
        else: 
            x = x-(funkcja2(x)/funkcja2p(x, 0.001))
    print("Przeproczono zakres iteracji")

print("Zadanie 4")
zadanie4(0)
zadanie4_1(0.5)