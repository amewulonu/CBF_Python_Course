import os

print("Current Working Directory:", os.getcwd())
print("List of files and directories in the current directory:", os.listdir('.'))
folder = os.path.join(os.getcwd(), 'test_folder')
os.makedirs(folder, exist_ok=True)
print("Created folder at:", folder)
file_path = os.path.join(folder, 'example.txt')
with open(file_path, 'w') as f:
    f.write("This is an example file.")
print("Created file at:", file_path)