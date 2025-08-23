import re

myString="Wel&*(*)come to pyt#$%hon programmer"
regex = re.compile('[@_!#$%^&*()<>?|\/{}~:]')
if regex.search(myString)==None:
    print("No special char")
else:
    print("special char")