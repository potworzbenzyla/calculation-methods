import numpy as np
import matplotlib as pylab

def funkcja1(x):
   return (x*x)+x-1

def funkcja2(x, delta):
    return (funkcja1(x+(delta/2)) - (x-(delta/2)))/delta

def zadanie5(pierwsza,druga,trzecia, delta):
    a = pierwsza
    b = druga
    
    if funkcja1(a)*funkcja1(b) > 0:
       return print("Brak rozwiazan")
    else:
        for k in range(10000):
          x = (a+b)/2 
          if funkcja1(a)*funkcja1(x) < 0:
              b = x
          else:
              a = x
          if np.abs(funkcja1(x)) < delta:
              print("Metoda bisekcji. Wynik pomiedzy ", a," i ", b,"Zakres znaleziony w ", k, " iteracji.")
              break
    
    a = pierwsza
    b = druga

    if funkcja1(a)*funkcja1(b) > 0:
        return print("3. Brak rozwiazan")
    for k in range(10000):
        x = a - ((funkcja1(a)/(funkcja1(b)-funkcja1(a))) * (b-a))
        if funkcja1(x)*funkcja1(a)<0:
            b = x
        else:
            a = x
        if np.abs(funkcja1(x)) < delta:
            print("Metoda siecznych. Wynik pomiedzy ", a, " i ", b, "Zakres znaleziony w ", k, " iteracji.")
            break

    a = trzecia
    x = trzecia

    for k in range(100000):
        if np.abs(funkcja1(x)) < delta:
            print("Metoda stycznych. Dla punktu poczatkowego " , a, ", pierwiastek równy ", x," znaleziony w ", k, " iteracji.")
            break
        else: 
            x = x - (funkcja1(x)/funkcja2(x, 2))

print("Zadanie 5")
zadanie5(0.05, 0.95, 0.95, 0.000001)