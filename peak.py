def peak_f(arr):
    flag=False
    if(arr[0]>arr[1]):
        flag=True
        return arr[0]
    else:
        for i in range(1,len(arr)-1):
            if(arr[i-1]<=arr[i]>=arr[i+1]):
                flag=True
                return arr[i]
    if(flag==False):
        return arr[len(arr)-1]

def peak_recur(list2):
    length=len(list2)
    if(length<=2):
        if list2[0]>list2[1]:
            return list2[0]
        return list2[1]
    if(list2[length//2-1]>list2[length//2]):
        peak_recur(list2[:length//2])
    elif(list2[length//2+1]>list2[length//2]):
        peak_recur(list2[length // 2:])
    else: return list2[length//2]


def it_peak(arr):
    if(arr[0]>arr[1]):
        return arr[0]
    else:
        for i in range(1,len(arr)-1):
            if(arr[i-1]<arr[i]>arr[i+1]):
                return arr[i]
    return arr[len(arr)-1]

def rec_peak(arr):
    if(len(arr)<=2):
        if(arr[0]>arr[1]):
            return arr[0]
        return arr[1]
    else:
        mid=len(arr)//2
        if(arr[mid]<arr[mid+1]):
            return rec_peak(arr[mid:])
        elif arr[mid-1]>arr[mid]:
            return rec_peak(arr[:mid])
        else:  return arr[mid]
num=input();
list1 = list(map(int, input().split()))
print(rec_peak(list1))