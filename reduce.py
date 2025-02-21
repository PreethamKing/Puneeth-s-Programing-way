import functools
from functools import reduce
n=5
result=reduce(int.__add__,range(1,n+1))
print(result)