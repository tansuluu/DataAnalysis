s=""
z=0
k=0
def func(j,a,b,c):
    global s
    global z
    if(a+b==c):
        z=1
    if(j<len(s)):
        func(j+1,a,b,c*10+int(s[j]))
def funb(j,a,b,c):
    global s
    if(j+1<len(s)):
        funb(j+1,a,b*10+int(s[j]),c)
    if(j<len(s)):
        func(j+1,a,b,c*10+int(s[j]))
def funa(j,a,b,c):
    global s
    global k
    if(j+2<len(s)):
        funa(j+1,a*10+int(s[j]),b,c)
    if(j+1<len(s) and j!=k):
        funb(j+1,a,b*10+int(s[j]),c)
        

num=int(input())
for i in range(0,num):
    s=input()
    z=0
    if(len(s)<3):
        print(0)
        continue
    for j in range(len(s)):
        k=j
        funa(j,0,0,0)
    if(z==1):
        print(1)
    else:
        print(0)
