#number of ways
def count_ways(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return 0
    else :
        return (count_ways(n-1) + count_ways(n-2) + count_ways(n-3))
    
num_stairs=int(input("Enter the number of stairs >> "))
print(count_ways(num_stairs))    