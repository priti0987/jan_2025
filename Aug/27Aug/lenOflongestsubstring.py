def longest_repeating_char_substring(s):
    max_char = ''
    max_len = 0
    current_char = ''
    current_len = 0

    for char in s:
        print(char)
        if char == current_char:
            current_len += 1
        else:
            current_char = char
            current_len = 1
        if current_len > max_len:
            max_len = current_len
            max_char = current_char

    return max_char * max_len

# Example usage
input_str = "aaaccddbbbbcd"
output = longest_repeating_char_substring(input_str)
print(output)  # Output: bbbb
