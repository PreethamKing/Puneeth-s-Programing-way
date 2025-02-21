string=input("Enter a string >> ")
vowel='aeiouAEIOU'
str_no_vowel="".join([char for char in string if char not in vowel ])
print(str_no_vowel)