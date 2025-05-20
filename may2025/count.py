# myString = "My name is priti "
# count = 1
# for i in myString:
#     if i == " ":
#         count = count +1
#
# # myString1 = myString.split(" ")
# for i in myString1:
#     if i.__contains__("p"):
#         print(i)
# print(count)

# a = 2
# b = '3.77'
# c = -8
# s = '{0:.4f} {0:3d} {2} {1}'.format(a, b, c)
# print(s)


# from array import *
#
# ai = array('i',[1,5,2,4,7,8])
# print(type(ai))
#
myString = "My name is priti"
def revMyString(string1):
    inString = string1.lower()
    inString = inString.replace(" ","")
    inString = list(inString)
    inString = inString[::-1]
    for i in range(len(string1)):
        if string1[i] == " ":
            print(i)
            inString.insert(i, " ")
        inString = "".join(inString[i])
        print(inString)
    return inString

print(revMyString(myString))
# # revString = myString[::-1]
# # print(revString)


# def reverse_words_and_order(input_string):
#     input_string=input_string.lower()
#     words = input_string.split()  # Split the string into words
#     words = words[::-1]  # Reverse the order of words
#     reversed_words = [word[::-1] for word in words]  # Reverse each word
#     output_string = ' '.join(reversed_words)  # Join the reversed words back into a string
#     return output_string.capitalize()
#
# input_string = "I am priti"
# output_string = reverse_words_and_order(input_string)
# print(output_string)