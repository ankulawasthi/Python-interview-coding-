def check_prime(num):
    count=0
    l=num//2
    for i in range(2,l+1):
        if num%2==0: 
            count+=1 
            break; 
    if count==1: 
        print("it is not a prime number")
    else: 
        print("it a prime number")
num=int(input("Enter a number: "))
check_prime(num)