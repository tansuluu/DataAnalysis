num=int(input());

for i in range(0,num):
    listRes = []
    res = ""
    n1=int(input())
    list1=[]
    list2=[]
    list1=list(map(int, input().strip().split()))
    for l in range(n1//2,n1):
        list2.append(list1[l])
    for t in range (0,n1//2):
        listRes.append(list1[t])
        listRes.append(list2[t])
    for p in range(0,len(listRes)):
        res+=str(listRes[p])+" "
    print(res)

        

    


        
              
