s = input()
digit=0
alpha=0
for i in range(0,len(s)):
    if(s[i].isdigit()):
        digit+=1
    if(s[i].isalpha()):
        alpha+=1
if(digit+alpha==len(s) and len(s)>=8 and digit >=2 ):
    print("Valid password")
else:
    print("Invalid password")