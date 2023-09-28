def armstrong_num(num):
    num1=num
    lnth=int(len(str(num)))
    arm_s=0
    while num!=0:
        ld=num%10
        arm_s += ld**lnth 
        num=num//10
    if arm_s == num1:
        return "it is a armstrong number"
    else: 
        return "it is not a armstrong number"

num=int(input("enteer a number:"))
print(armstrong_num(num))