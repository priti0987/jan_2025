import os

target_directory = "C:\\"
try:
    contents = os.listdir(target_directory)
    print(f"Contents of {target_directory}:")
    for item in contents:
        print(item)
        print( item.__getstate__())
except FileNotFoundError:
    print(f"Directory not found: {target_directory}")
except PermissionError:
    print(f"Permission denied to access: {target_directory}")