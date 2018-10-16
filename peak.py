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
num=input();
list1 = list(map(int, input().split()))
print(peak_recur(list1))