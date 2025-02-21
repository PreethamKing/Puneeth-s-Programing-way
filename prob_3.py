number=[-2, -1, 0, 1, 2]
print(sorted(list(map(abs,filter(lambda x:x<0,number)))))