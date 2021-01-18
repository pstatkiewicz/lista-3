import matplotlib.pyplot as plt
def how_many_letters(string):
    string.lower()
    counter=[0]*26
    letters=[]
    list1=[]
    for i in range(26):
        letters.append(chr(97+i))
    for i in range(len(string)):
        if ord(string[i])<123 and ord(string[i])>96:
            counter[ord(string[i])-97]+=1
    for i in range(26):
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
