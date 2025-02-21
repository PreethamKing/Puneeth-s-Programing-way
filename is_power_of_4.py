def is_power_of_4(n):
    if n==1:
        return 'T'
    elif n==0:
        return 'F'
    else :
        return is_power_of_4(n//4)

num=int(input("Enter the number which should be checked >> "))
print(is_power_of_4(num))        