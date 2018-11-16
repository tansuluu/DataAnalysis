num=int(input())
list1=list(map(int,input().strip().split()))
mid=num//2
list2=[]
list3=[]
flag=True
flag2=True
for i in range(0,num):
    if i<mid:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
for i in range(1,len(list2)):
    if(list2[i-1]<=list2[i]):
        flag=False
print(list2)
for i in range(1,len(list3)):
    if list3[i-1]>=list3[i]:
        flag2=False
print(list3)
if(flag==True and flag2==True):
    print("Yes")
else: print("No")