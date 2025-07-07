# class Student:
#     name = "priti"
#     def __init__(self):
#         print("starting of obj .. ")
#
# p = Student()
# print(p.name)
#create student class that takes name & marks of 3 sub as arguments in constructor

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum = sum+i
        avgg = sum/len(self.marks)
        print("Hi ",self.name ,"Your avg score is ", avgg)

s1 = Student("priti",[99,55,66])
s1.avg()
