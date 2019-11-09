import os

def find_files(suffix, path):
    if suffix is None or path is None:
        print("Empty input")
        return
    
    elif os.path.exists(path) is False:
        print("Invalid path")
        return
        
    contents = os.listdir(path)
    
    if len(contents) == 0:
        return []
        
    suffix_files = [file for file in contents if suffix in file]
        
    folder_list = [folder for folder in contents if os.path.isdir(path + '/' + folder) is True]
        
    for folder in folder_list:
        suffix_files.extend(find_files(suffix, path + '/' + folder))    
        
    return suffix_files

print("\n")
print("Normal test")
suffix = '.c'
path = os.getcwd()
print(find_files(suffix, path))

print("\n")
print("Edge Test 1: empty input")
suffix = None
path = os.getcwd()
find_files(suffix, path)

print("\n")
print("Edge Test 2: invalid address")
suffix = '.c'
path = 'home/user'
find_files(suffix, path)