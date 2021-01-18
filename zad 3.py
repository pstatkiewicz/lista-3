def rot13(string):
    for i in range(len(string)):
        if (ord(string[i])>64 and ord(string[i])<91) or (ord(string[i])>96 and ord(string[i])<123):
            variable=ord(string[i])+13
            if variable>90 and variable<104:
                variable-=26
            if variable>122 and variable<136:
                variable-=26
            print(chr(variable),end='')
        else:
            print(string[i],end='')
text=input("Podaj tekst:")
rot13(text)
