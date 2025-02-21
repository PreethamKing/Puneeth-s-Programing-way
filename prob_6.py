strings_li = ["PYTHON", "computational", "PROBLEM", "solving"]
sub_result=tuple(map(str.capitalize,filter(str.isupper,strings_li)))
sub_result1=tuple((filter(lambda x: False if x.isupper()==True else True,strings_li)))
print(sub_result+sub_result1)