def count_unique_characters(input_string):
    unique_chars = set()

    for char in input_string:
        unique_chars.add(char)

    return len(unique_chars)

input_str = "Guvi Geeks Network Private Limited"
result = count_unique_characters(input_str)
print("Number of unique characters:", result)
