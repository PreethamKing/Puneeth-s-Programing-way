# Function that filters vowels
letter="aeiouAEIOU"
characters = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r','l','d']
result=list(filter(lambda x:x in letter,characters))
print(result)