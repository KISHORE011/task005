def is_palindrome(input_str):
    cleaned_str = ''.join(input_str.split()).lower()
    
    return cleaned_str == cleaned_str[::-1]

print(is_palindrome("RACECAR"))  # True
print(is_palindrome("KISHORE"))    # False
print(is_palindrome("MALAYALAM"))  # True

