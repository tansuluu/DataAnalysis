n=input();
listA=[];
result="";
for i in n:
    word=input();
    half=len(word)//2;
    wor=word[0:half];
    s=0;
    for k in wor:
        if s%2==0:
            result+=k;
        s+=1;
    listA.append(result);
for l in listA:
 print(l);
