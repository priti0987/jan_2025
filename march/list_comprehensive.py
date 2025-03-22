#list of square , in range of 10
# i**i means i raise to i
# i*i means square
# i**2 means square
# mylist = [i*i for i in range(1,11)]
# print(mylist)
#filtering even numbers
# mylist1= [i for i in range(1,11) if i%2==0]
# print(mylist1)
#flatering list of lists
# givenList = [[1,2,3],[4,5,6],[7,8,9]]
# newList = [j for i in givenList for j in i]
# print(newList)

#generating a list of first letters of words in a list
# mywords=["bhavika","pratap","anvit","neel"]
# word = [i[0] for i in mywords]
# print(word)

#generating list of sqaure of even numbers

# sqr_evenNumbers = [ i**2 for i in range(1,11) if i%2==0]
# print(sqr_evenNumbers)

#converting list of string  to a list of integers
# mylistt = ['1','2','4','6']
# intList = [int(i) for i in mylistt]
# print(intList)
#generating a list of fibonacci sequence
# fib =[0,1,1,2,3,5,8,13,21]
# myfib = [fib[i-1]+fib[i-2] for i in range(2,len(fib))]
# print(myfib)

#generating a list of all divisors of a numbers
# number =100
# divrss = [i for i in range(1,number+1) if number%i==0]
# print(divrss)

#genrating prime number less than given number