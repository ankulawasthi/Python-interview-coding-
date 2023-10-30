#Write a Python program to count the frequency of each element in a llist

def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency
arr=[1,2,3,1,3,1,3,4,5,4,3,5]
print(count_frequency(arr))

        
