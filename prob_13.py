#Find the sum of digits of a number entered by the user
n=int(input("Enter a number >> "))
def add(x):
    s=0
    for i in str(x):
        s+=int(i)
    return s
print("sum =",add(n))
