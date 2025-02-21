#Function to check whether a number is a multiple of 3 using Lambda function in filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=list(filter(lambda x:x%3==0,numbers))
print(result)