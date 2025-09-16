abc="bbbbbbbccfffffffeeeaaeeeezzzzzzzzzzzzze"
l=list(set(list(abc)))
l.sort()
print(''.join(l))
#remove all repeatative letters