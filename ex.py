j,k=map(int,input().strip().split())
l,n=map(int,input().strip().split())
fistMatr=[]
secondMatr=[]
result=[]
for b in range (j):
    ar=[]
    for a in range(n):
        ar.append(0);
    result.append(ar)
for s in range(j):
    listTemp=list(map(int,input().strip().split()))
    fistMatr.append(listTemp)

for p in range(l):
    listTemp=list(map(int,input().strip().split()))
    secondMatr.append(listTemp)
print(result)

for i in range(len(fistMatr)):
   for j in range(len(secondMatr[0])):
       for k in range(len(secondMatr)):
           result[i][j] += fistMatr[i][k] * secondMatr[k][j]

print(result)