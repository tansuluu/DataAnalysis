def sortingI(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while key<arr[j] and j>0:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
print(sortingI([1,6,2,3,6]))



