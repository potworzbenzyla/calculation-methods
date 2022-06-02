import numpy as np
import matplotlib as pylab

def f1(x):
   return (np.exp(5*x)/100)-(1/4)

def f2(x, delta):
    return ( f1( x+(delta/2) ) - ( x-(delta/2) ) )/delta

def f3(x):
   return -np.exp((-5)*x)+(1/4)

def f4(x):
   return np.exp((-5)*x)-(1/4)

def f5(x):
   return (-np.exp(5*x)/100)+(1/2)

def zadanie2_1(a,b):
    if f1(a)*f1(b)>0:
        return print("1. Brak rozwiazan")
    for k in range(1000):
        x = a - ( ( f1(a) / ( f1(b)-f1(a) ) ) * (b-a))
        if f1(x)*f1(a)<0:
            b = x
        else:
            a = x
    print("1. Wynik pomiedzy ",a," i ", b)
    
def zadanie2_2(a,b):
    if f3(a)*f3(b)>0:
        return print("2. Brak rozwiazan")
    for k in range(1000):
        x = a - ( ( f3(a) / ( f3(b)-f3(a) ) ) * (b-a))
        if f3(x)*f3(a)<0:
            b = x
        else:
            a = x
    print("2. Wynik pomiedzy ",a," i ", b)
               
def zadanie2_3(a,b):
    if f4(a)*f4(b)>0:
        return print("3. Brak rozwiazan")
    for k in range(1000):
        x = a - ( ( f4(a) / ( f4(b)-f4(a) ) ) * (b-a))
        if f4(x)*f4(a)<0:
            b = x
        else:
            a = x
    print("3. Wynik pomiedzy ",a," i ", b)
    
def zadanie2_4(a,b):
    if f5(a)*f5(b)>0:
        return print("4. Brak rozwiazan")
    for k in range(1000):
        x = a - ( ( f5(a) / ( f5(b)-f5(a) ) ) * (b-a))
        if f5(x)*f5(a)<0:
            b = x
        else:
            a = x
    print("4. Wynik pomiedzy ",a," i ", b)

print("Zadanie 2")

zadanie2_1(0.05,0.95)
zadanie2_2(0.05,0.95)
zadanie2_3(0.05,0.95)
zadanie2_4(0.05,0.95)