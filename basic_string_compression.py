def compress_string_recursive(s, index=0, count=1, result=''):
    if index == len(s) - 1:
        return result + s[index] + str(count)
    
    if s[index] == s[index + 1]:
        return compress_string_recursive(s, index + 1, count + 1, result)
    else:
        result += s[index] + str(count)
        return compress_string_recursive(s, index + 1, 1, result)


print(compress_string_recursive('aabcccccaaa'))