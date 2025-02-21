#to flattent nested list
def to_flattend(_input_list):
    flattend=[] 
    for i in _input_list:
        if type(i)==int:
            flattend.append(i)
        else :
            return flattend.extend(to_flattend(i))
    return flattend
        
print(to_flattend([1]))
