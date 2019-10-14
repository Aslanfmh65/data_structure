import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if os.path.exists(path) is False:
        return []
        
    contents = os.listdir(path)
    
    if len(contents) == 0:
        return []
        
    suffix_files = [file for file in contents if suffix in file]
        
    folder_list = [folder for folder in contents if os.path.isdir(path + '/' + folder) is True]
        
    for folder in folder_list:
        suffix_files.extend(find_files(suffix, path + '/' + folder))    
        
    return suffix_files

suffix = '.c'
path = os.getcwd()
files = find_files(suffix, path)
print(files)