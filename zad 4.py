def rot13(string):
    for i in range(len(string)):
        if (ord(string[i])>64 and ord(string[i])<91) or (ord(string[i])>96 and ord(string[i])<123):
            variable=ord(string[i])-13
            if variable<97 and variable>83:
                variable+=26
            if variable<65 and variable>51:
                variable+=26
            print(chr(variable),end='')
        else:
            print(string[i],end='')
    print("\n")
text1="N zna, n cyna, n pnany: Cnanzn!"
text2="N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF: 1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzrag jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr fpvragvsvp bowrpgvivgl. 2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvat yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg. 3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ. Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb hcubyq."
rot13(text1)
rot13(text2)

