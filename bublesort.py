def bublesort(arr):
    for i in range(0, len(arr)):
        for k in range(0, len(arr)-i-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr;

print(bublesort([5,2,1,7,3]))