import numpy as np
import matplotlib as pylab

def funkcja(x):
   return (x*x)+x-1

def zadanie1(a,b):
   if f(a)*f(b)>0:
      return print("Brak rozwiazan")
   else:
       for k in range(100):
         x = (a+b)/2
         if np.abs(f10(x))<0.001:
             return print("Wynik pomiedzy ",a," i ", b,"Zakres znaleziony w ", k, " iteracji.")
         else: 
             if funkcja(a)*funkcja(x)<0:
                 b = x
             else:
                a = x
       print("Wynik pomiedzy ",a," i ", b)
       
   x = pylab.arange(0.05, 0.95, 0.01)
   y = (x*x)+x-1

   pylab.plot(x,y,'r--')
   pylab.title("Zadanie 1")
   pylab.xlabel("x")
   pylab.ylabel("y")
   pylab.show

print("Zadanie 1")
zadanie1(0.05, 0.95
