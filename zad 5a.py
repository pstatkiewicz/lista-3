def NWD_iteration(a, b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
print("Podaj długość listy: ")
n=int(input())
numbers=[]
results=[]
print("Podaj liczby: ")
for i in range(n):
    x=int(input())
    numbers.append(x)
for i in range(len(numbers)):
    for j in range(1,len(numbers)-i):
        results.append((NWD_iteration(numbers[i],numbers[i+j])))
results.sort(reverse=False)
print(results[0])
