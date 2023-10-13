#Sum of square n natural number
def sum_sqr(n):
    sum=0
    for i in range(1,n+1):
        print(i**2)
        sum+=i**2
    return sum 
n=5 
print(sum_sqr(n))
    