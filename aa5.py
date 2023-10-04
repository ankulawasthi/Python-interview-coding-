#Factorial of a number using recursion 
'''def factorial_num(num):
    if num == 0 or num==1:
        return 1 
    else:
        return num*factorial_num(num-1) 
    
print(factorial_num(5))
    '''
# 2nd mothed using math module 

import math
def fact(num): 
    return math.factorial(num)
print(fact(5))