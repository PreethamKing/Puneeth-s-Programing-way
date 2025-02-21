m = [23,45,67] 
n = [12,65,98,23,55]

def result(m,n):
    result1=[]
    for i in m:
        result1.append(i)
        for j in n:
            result1.append(j)
    return result1    
print(result(m,n))