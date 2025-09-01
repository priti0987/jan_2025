# def get_odd_letters(message):
#     odd_letters = []
#     for counter in range(0, len(message)):
#         if not is_even(counter):
#             odd_letters.append(message[counter])
#
#     return odd_letters
#
#
# def get_even_letters(message):
#     even_letters = []
#     for counter in range(0, len(message)):
#         if is_even(counter):
#             even_letters.append(message[counter])
#
#     return even_letters
#
#
# def is_even(numb):
#     return numb % 2 == 0
#
# print("odd letters ",get_odd_letters("priti"))
# print("even letters ",get_even_letters("priti"))


myString = "priti"

for i in range(len(myString)):
    if i%2!=0:
        print(myString[i])