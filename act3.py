num=int(input())
list1=list(map(int, input().strip().split()))
num2=int(input())
list2=list(map(int,input().strip().split()))
for i in range(0,num):
    if list1[i]==list2[i]:
        print(i+1)