# Find the largest number in array 
def arr_lnum(arr):
    mx = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > mx: 
            mx=arr[i] 
    return mx 
arr=list(map(int,input().split()))
print(arr_lnum(arr))
