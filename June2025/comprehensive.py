nums =[1,5,3,6,9,5,44]

mylist = [n*2 for n in nums]
#print(mylist)
even=[n for n in nums if n%2==0]
#print(even)
onlyOdd=[2*n-1 for n in nums]
print(onlyOdd)
podd = [n+1 for n in nums if n%2==0]
print(podd)