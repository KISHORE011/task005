def remove_vowels(input_string):
    vowels = "AEIOUaeiou"
    result = ""
    
    for char in input_string:
        if char not in vowels:
            result += char
    
    return result

# Example usage:
input_str = "Guvi Geeks Network Private Limited"
result_str = remove_vowels(input_str)
print(result_str)  

