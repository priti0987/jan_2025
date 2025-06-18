nums =[1,5,3,6,9,5,44]

mylist = [n*2 for n in nums]
#print(mylist)
even=[n for n in nums if n%2==0]
#print(even)
onlyOdd=[2*n-1 for n in nums]
#print(onlyOdd)
podd = [n+1 for n in nums if n%2==0]
# print(podd)

mylist = [(let,num) for let in 'abcd' for num in range(4)]
# print(mylist)

name = ['pandurange','pratibha','pallavi','priya','priti']
role = ['father','mother','eldersister','twin sis1','twin sis2']
# fam_1= [(zip(name,role))]
# print((fam_1))
myfDictionary = {name : role for name ,role in zip(name,role)}
# print(myfDictionary)
myset ={n for n in name}
print(myset)
print(type(myset))