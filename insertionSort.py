num=int(input("Enter the length of array"))
list1=[]
for i in range(0,num):
    list1.append(input())

def insertSort(arr):
    for i in range(1,len(arr)):
        for k in range(0,i):
            if(arr[k]>arr[i]):
                arr[i],arr[k]=arr[k],arr[i]
    return arr
print(insertSort(list1))

