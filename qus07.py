def most_frequent_char(input_string):
    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    most_frequent = max(char_count, key=char_count.get)

    return most_frequent

input_str = "Guvi Geeks Network Private Limited"
result = most_frequent_char(input_str)
print(f"The most frequent character is '{result}'")
