#to find sum
def add(n):
    if n==0:
        return 0
    else :
        return (n%10+add(n//10))


num=int(input("Enter the a number >> "))
print(add(num))
    