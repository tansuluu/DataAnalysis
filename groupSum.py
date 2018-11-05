def group_sum(start,arr,target):
    if start>=len(arr):
        return target==0
    if(group_sum(start+1,arr,target-arr[start])):
        return True
    if (group_sum(start + 1, arr, target)):
        return True;
    return False

def str_copy(str,sub,n):
    print(func(str,sub))
    if(func(str,sub)==n):
        return True
    else: return False

def func(str,sub):
    print(str,"str")
    if(len(str)<len(sub)):
        return 0
    elif(str[:len(sub)]==sub):
        return 1+func(str[1:],sub)
    else: return func(str[1:],sub)

print(str_copy("catcowcat", "cat", 2))