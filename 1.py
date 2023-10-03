#write a program reverse of a number 
def reverse_num(num):
    rev=0   
    while num!=0:   
        ld = num%10   
        rev = rev*10+ld    
        num = num//10 
    return rev 
print(reverse_num(199))    

    