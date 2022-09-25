s = input()
string=s.upper()
for i in range(0,12):
    if(string[i] in ['0','1','2','3','4','5','6','7','8','9']):
        print(string[i],end='')
    if(string[i]=='-'):
        print("-",end='')
    if (string[i] in['A','B','C']):
        print(2,end='')
    if (string[i] in['D','E','F']):
        print(3,end='')
    if (string[i] in['G','H','I']):
        print(4,end='')
    if (string[i] in['J','K','L']):
        print(5,end='')
    if (string[i] in['M','N','O']):
        print(6,end='')
    if (string[i] in['P','R','Q','S']):
        print(7,end='')
    if (string[i] in['T','U','V']):
        print(8,end='')
    if (string[i] in ['W', 'X', 'Y','Z']):
        print(9, end='')