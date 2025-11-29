myString ="Priti"

occ={}
index=0

for ch in myString:
    if ch not in occ:
        occ[ch]=index
    index=index+1

print(occ)