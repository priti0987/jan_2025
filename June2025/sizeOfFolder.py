# import module
import os

# assign size
size = 0

# assign folder path
Folderpath = 'C:\13March'

# get size
for path, dirs, files in os.walk(Folderpath):
    print(path)
    print(dirs)
    print(files)
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

# display size
print("Folder size: " + str(size))