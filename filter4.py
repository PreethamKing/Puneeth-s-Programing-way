# To pickup all words whose length exceeds 5 using map,filter and Lambda function.
Names=[ 'Ram', 'Tejas', 'Aditya', 'Ravi', 'Dinesh', 'Raghu' ]
print(list(map(str.upper,filter(lambda x:len(x)>5,Names))))
