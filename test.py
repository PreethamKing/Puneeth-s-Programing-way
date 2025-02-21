#filter even and odd
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = list(filter(lambda x:x%2 != 0, num_list))
even_list = list(filter(lambda x:x%2 == 0, num_list))

def lower_upper(ls):
    upper_no = 0
    lower_no = 0
    for i in ls :
        if i.islower() == True :
            lower_no += 1
        else :
            upper_no += 1
    print("No of lower is ",lower_no)
    print("no of upper is ",upper_no)
    
def  gcd(m,n) :
    if n == 0 :
        return m
    else :
        return gcd( n,m%n )