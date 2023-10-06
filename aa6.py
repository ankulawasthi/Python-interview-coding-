#Python Program for n-th Fibonacci number

def fibo_num(n):
    if n==1:
        return 0 
    elif n==2: 
        return 1 
    else: 
        return fibo_num(n-1) + fibo_num(n-2)
n=5
for i in range(1,n+1):
    print(fibo_num(i))