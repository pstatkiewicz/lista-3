import math
def binomial_theorem(a,b):
    result=int(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))
    return result
def Pascal_Triangle(n):
    for i in range(0,n+1):
        print(" "*(n-i),end=" ")
        for j in range(0,i+1):
            print(binomial_theorem(i,j),end=" ")
        print()
print("Podaj stopień: ")
n=int(input())
Pascal_Triangle(n)
