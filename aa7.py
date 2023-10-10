#Given array remove duplicate element 
def remove_duplicate(arr): 
    rd=[]
    for i in range(len(arr)):
        if arr[i] not in rd:
            rd.append(arr[i])
    return len(rd) 
arr=list(map(int,input().split()))
print(remove_duplicate(arr))
    




