import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=True):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                if not os.path.islink(filepath):
                    total_size += os.path.getsize(filepath)
            except Exception:
                # Ignore files that cannot be accessed
                continue
    return total_size

def convert_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024

def list_folders_in_drive(drive_path):
    try:
        for item in os.listdir(drive_path):
            folder_path = os.path.join(drive_path, item)
            if os.path.isdir(folder_path):
                try:
                    size = get_folder_size(folder_path)
                    print(f"{folder_path}: {convert_size(size)}")
                except PermissionError:
                    print(f"{folder_path}: [Permission Denied]")
    except Exception as e:
        print(f"Failed to access {drive_path}: {e}")

# Run for C:\ drive
drive = "C:\\"
print(f"Calculating folder sizes in {drive}...\n")
list_folders_in_drive(drive)
