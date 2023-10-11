def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count1 = {}
    char_count2 = {}
    
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    return char_count1 == char_count2

string1 = "video game"
string2 = " give a demo"
result = is_anagram(string1, string2)
print(result)  
