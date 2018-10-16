num=int(input());
for i in range(0,num):
    n,x,y=map(int, input().split())
    for k in range(1,n):
        if k%x==0 and k%y!=0:
            print(k);
