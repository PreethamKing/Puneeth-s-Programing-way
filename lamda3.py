def myfunction(n):
    return lambda a : a*n
double_N=myfunction(2)
print(double_N(4))