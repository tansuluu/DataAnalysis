def mergeSort(arr,start, end):
    if(start<end):
        mid=int((start+end-1)/2)
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        combineMerge(arr,start,mid,end)

def combineMerge(arr,start,mid,end):
    n1=mid-start
    n2=end-mid;
    l1=[]
    l2=[]
    for k in range (0,n1):
        l1[k]=arr[start+k-1]
    for l in range(0,n2):
        l2[l]=arr[mid+l-1]
    i=0
    j=0
    for t in range(start,end):
        if(l1[i]<=l2[j]):
            arr[t]=l1[i]
            i=i+1
        else:
            arr[t]=l2[j]
            j=j+1

print(mergeSort([4,2,6,1],0,3))