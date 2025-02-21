#Use of lambda function to filter out the odd and even numbers from a list
sequence = [0,1, 1, 2, 3, 5, 8,19]
even=list(filter(lambda x:x%2==0,sequence))
odd=list(filter(lambda x:x%2!=0,sequence))
print("even",even)
print("odd",odd)