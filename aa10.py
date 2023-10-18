# difference between the count of odd numbers and even numbers.
def diff_eo(arr):
    en=[]
    od=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            en.append(arr[i])
        else: 
            en.append(arr[i])
    return abs(len(en)-len(od))

arr=list(map(int,input().split()))
print(diff_eo(arr))


