numbers = [9, 12, 4, 2, 7]
print(list(map(lambda x:(x+1) if x%2==0 else (x-1),numbers)))