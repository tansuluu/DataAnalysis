n = int(input())
for i in range(n):
    num=input()
    sum=0
    for k in range(len(num)):
        sum+=int(num[k])
    print(sum)
