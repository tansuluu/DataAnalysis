def mergeS(arr,l,r):
    if(r>l):
        m=(r+l-1)//2
        mergeS(arr,l,m)
        mergeS(arr,m+1,r)
        comb(arr,l,m,r);
    return arr

def comb(arr,l,m,r):
    n1=m-l+1;
    n2=r-m;
    L=[0]*n1
    R=[0]*n2

    for i in range(0,n1):
        L[i]=arr[l+i]

    for k in range(0,n2):
        R[k]=arr[m+k+1]

    k=l
    j=0
    i=0
    while j<n1 and i<n2:
        if L[j]<=R[i]:
            arr[k]=L[j]
            j=j+1
        else:
            arr[k]=R[i]
            i=i+1
        k=k+1

    while j<n1:
        arr[k]=L[j]
        j=j+1

    while i<n2:
        arr[k]=R[i]
        i=i+1
    return arr

print(mergeS([9, 6, 1, 9, 7],0,4))