num=int(input());
for i in range(0,num):
    k,j=map(int, input().split())
    res="";
    for l in range(0,k*j):
        if l<j or l%j==0 or l%j==j-1 or l>(k-1)*j:
            res+="*";
        else:
            res+=".";
        if (l+1)%k==0:
            print(res)
            res=""
