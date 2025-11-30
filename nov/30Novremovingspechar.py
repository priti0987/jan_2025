inputString = "w12#$e2@lc^*&o)(m:><e"
outputString = "welcome"
newString = ""
for ch in inputString:
    if ch.isalpha():
        newString = newString +ch

print(newString)