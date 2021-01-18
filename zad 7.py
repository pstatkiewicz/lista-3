import math
def quadratic(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        return "Równanie nie ma pierwiastków rzeczywistych"
    if a==b==c==0:
        return "Rozwiązanie ma nieskończenie wiele rozwiązań"
    if a==b==0:
        return "Równanie nie ma pierwiastków rzeczywistych"
    if a==0:
        return -c/b
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    return x1,x2
print("Podaj kolejne współczynniki wielomianu:")
a=float(input())
b=float(input())
c=float(input())
print(quadratic(a,b,c))
