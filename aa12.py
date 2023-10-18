#count the unique character in given string 

def count_uc(string):
    s=""
    for i in string:
        count = 0
        for j in string:
            if i == j:
                count+=1 
            if count > 1:
                break 
        if count == 1:
            s+=i 
    return len(s)

string="ababm"
print(count_uc(string))

    
