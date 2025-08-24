import os

pathOfFile = "C:\\Users\\Dell\\Desktop\\today.txt"

# f = open(pathOfFile)
# # print(f.read())
# if (f.read().__contains__("pri3454ti")):
#     print("pass")
# else:
#     print("Not found")


# with open(pathOfFile) as f:
#   print(f.read())
#   print("pass.........")
filePathh = "c:\\Users\\Dell\Desktop\\24AugNewtext.txt"
f = open(filePathh, "x")
f.write("hi.. Priti..")
f.close()
f = open(filePathh)

print(f.read())
f.close()

DeleteFile = input("enter y if u wanaa delete this file : ")
if DeleteFile == 'y':
    os.remove(filePathh)
    print("Done..")