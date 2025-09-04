#convert to upper case without upper method
from wsgiref.util import request_uri


def to_upper(s):
    result = ""
    for i in s:
        # print(i) Ascii a = 97
        if 'a'<=i<='z':
            result+=chr(ord(i)-32)
        else:
            # print(i)
            result+=i
    return result

def to_lower(s):
    result = ""#ascci of A = 65
    for i in s:
        if 'A'<=i<='Z':
            result+=chr(ord(i)+32)
        else:
            result+=i
    return result



print(to_upper('prIti'))
print(to_lower("PriTi"))
