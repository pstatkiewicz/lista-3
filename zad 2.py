import matplotlib.pyplot as plt
def how_many_letters(string):
    string.lower()
    letters='aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    counter=[0]*len(letters)
    list1=[]
    for j in range(len(string)):
        for i in range(len(letters)):
           if string[j]==letters[i]:
               counter[i]+=1
    for i in range(len(letters)):
        list1.append([counter[i],letters[i]])
    list1.sort(reverse=True)
    result=list1[0:10]
    counter1=[]
    letters1=[]
    for i in result:
        counter1.append(i[0])
        letters1.append(i[1])
    plt.bar(letters1,counter1)
    plt.title("Częstotliwość występowania liter")
    plt.show() #matplotlib
    return result #print
print("Podaj tekst: ")
text=input()
print(how_many_letters(text))
