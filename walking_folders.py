import os

START = "."

SKIP = '.git'

for folder, dirs, files in os.walk(START):
    if SKIP in dirs:
        dirs.remove(SKIP)
    print(folder)
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print(f"{file_size:8d} {file_name}")
