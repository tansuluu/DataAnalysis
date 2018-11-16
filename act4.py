num,x=map(int,input().strip().split())
list1=list(map(int,input().strip().split()))
list2=list(map(int,input().strip().split()))
for i in range(0,num):
    for y in range(-x,x+1):
        if(i+y<num and i+y>0 and list1[i]==list2[i+y]):
            print(i+1)
