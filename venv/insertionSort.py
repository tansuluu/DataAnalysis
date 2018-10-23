

def insertSort(arr):
    for i in range(1,len(arr)):
        for k in range(0,i):
            if(arr[k]>arr[i]):
                arr[i],arr[k]=arr[k],arr[i]
    return arr
print(insertSort([3,4,1,2,7,5]))

