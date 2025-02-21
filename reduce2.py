import functools
from functools import *
temperature = [5,2,6,7]
sum=reduce(int.__add__,temperature)
print(sum)