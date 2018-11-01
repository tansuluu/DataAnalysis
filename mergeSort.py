def mergeSort(arr,start, end):
    if(start<end):
        mid=int((start+(end-1))/2)
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        combineMerge(arr,start,mid,end)

def combineMerge(arr,start,mid,end):
    n1=mid-start+1
    n2=end-mid;
    l1=[0]*(n1)
    l2=[0]*(n2)
    for k in range (0,n1):
        l1[k]=arr[k+start]
    for l in range(0,n2):
        l2[l]=arr[mid+l+1]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = 0 # Initial index of merged subarray

    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = l1[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while i < n1:
        arr[k] = l1[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = l2[j]
        j += 1
        k += 1


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print(n)
for i in range(n):
	print ("%d" %arr[i]),

mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
	print ("%d" %arr[i]),