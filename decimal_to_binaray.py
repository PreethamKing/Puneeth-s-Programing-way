#to convert form decimal to binary
def decimal_to_binary(n):
    if n==0:
        return 0
    elif n==1 :
        return 1
    else :
        return(str(n%2)+str(decimal_to_binary(n//2)))   

num=int(input("enter the number that should be converted >>  "))
print(decimal_to_binary(num))
