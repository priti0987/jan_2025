

def remove_duplicates_from_string(s):
    result = ""
    for i in s:
        if i not in result:
            result = result+ i
    return result


myString = "priti"
cleanString = remove_duplicates_from_string(myString)
print(cleanString)