#regular expression 7 march
import re
text = '''
Priti priya Ok '''

pattern = r"[A-Z]"
matchh = re.finditer(pattern,text)
print(matchh)
for i in matchh:
    print(i)