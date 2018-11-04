num=int(input());

for i in range(num):
    k,j=map(int, input().split())
    res="";
    for l in range(0,k*j):
        if l%2==0:
            res+="*"
        else:
            res+=".";
        if (l+1)%j==0:
            print(res)
            res=""
    
        
