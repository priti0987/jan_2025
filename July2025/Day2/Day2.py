#find longest word from string

s = "I love programming python"
words = s.split(" ")
longestWord = words[0]
for i in words:
    if len(longestWord) < len(i):
        longestWord =i
print(longestWord)

# remove duplicates and maintain the order from string
s = "hello world hello"
se = set(s)
print("".join(se))

def first_non_repeating_char(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None  # or return '' if you prefer

# Example usage: non-repeating character
input_str = "aabbcde"
output = first_non_repeating_char(input_str)
print(output)  # Output: c

myCount = 0
myString ="hjhgarerrAREROIUO"
myString= myString.lower()
for i in myString:
    if i in "aeiou":
        myCount = myCount+1
print(myCount)

