from math import *

#function definition here
def f(x):
    return x ** 2  #x^2
#For instance f(2) = 4


def derive(function, value):
    h = 0.00000000001
    slope = (function(value + h) - function(value)) / h

    # Returns the slope to the third decimal
    return float("%.3f" % slope)

print(f(2))
print("A")
print (derive(f,2))

def g(x): #Second function
    return sin(x) * cos(x) + exp(2*x) + 2*x**4 - 10

print(g(-1))
print(derive(g, -1))