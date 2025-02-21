with_dots = ["PYTHON..", ".computational..", "..PROBLEM", "solving..", "for", "first", "ye..ar."]
print(list(map(lambda x:x.strip("."),with_dots)))#to remove leading and trading dots
print(list(map(lambda x:x.replace(".",""),with_dots)))#to remove all dots 