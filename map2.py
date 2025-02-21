#Function that doubles even numbers present in the list
func=lambda n:n*2 if n%2==0 else  n  
list1=[1,2,3,4,5,6]
result = map(func,list1)
print(list(result))