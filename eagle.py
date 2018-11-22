import math
num=int(input())
max=0
list3=[]
index=0
for i in range(0, num):
    numin=int(input())
    for k in range(0,numin):
        m,p=map(int, input().strip().split())
        result=math.sqrt(m*m+p*p)
        p=0
        if max<result:
            max=result
            index=k
    list3.append(index+1)

for y in range(0, len(list3)):
    print("farthest planet ", y+1,": ",list3[y])