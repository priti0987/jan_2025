#find longest word from string

s = "I love programming python"
words = s.split(" ")
longestWord = words[0]
for i in words:
    if len(longestWord) < len(i):
        longestWord =i
# print(longestWord)

# remove duplicates and maintain the order from string
s = "hello world hello"
se = set(s)
print(se)
