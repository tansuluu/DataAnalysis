j,k=map(int,input().strip().split())
l,n=map(int,input().strip().split())
fistMatr=[]
secondMatr=[]
for s in range(j):
    listTemp=list(map(int,input().strip().split()))
    fistMatr.append(listTemp)

for p in range(l):
    listTemp=list(map(int,input().strip().split()))
    secondMatr.append(listTemp)
for y in range(0,j):
    for z in range(0,l):
        l.append(0)
    result.append(l)


for i in range(len(fistMatr)):
   for j in range(len(secondMatr[0])):
       for k in range(len(secondMatr)):
           result[i][j] += fistMatr[i][k] * secondMatr[k][j]

print(result)