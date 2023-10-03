# Write a python code add two number without using + 
def add_twonum(num1,num2): 
    while num2!=0: 
        num1+=1
        num2-=1 
    return num1
print(add_twonum(5,6))
