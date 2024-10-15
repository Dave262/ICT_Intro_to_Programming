import os
import shutil
from typing import List

# declare folder and file list variables to be filled later
folder_list = []
file_list = []

# declare a path and print it for good measure
file_path: str = "./containing_folder"
print(f"the file path is: {file_path}")

folder_path: str = "./folder_folder"
print(f"the folder path is: {folder_path}")

# put files from path in a list
file_contents: List[str] = os.listdir(file_path)
for item in file_contents:
        file_list.append(item)
        print(file_list)

# put folder names in a list 
folder_contents: List[str] = os.listdir(folder_path)
for item in folder_contents:
    # if os.path.isdir(os.path.join(file_path, item)):
        folder_list.append(item)
        print(folder_list)

def remove_suffix(filename: str, suffixes: List[str]) -> str:
    for suffix in suffixes:
        if filename.lower().endswith(suffix.lower()):
            return filename[:-len(suffix)]
    return filename


# Iterate through file_list and match files and folder then move the files into matched folders    
for file in file_list:
    print (f"file: {file}")
    for folder in folder_list:
        if file.removesuffix(".txt") == folder: # could make a function to remove all suffix. 
            print("there's a match!")
            src_path = os.path.join(file_path, file)
            dst_path = os.path.join(folder_path, folder, file)
            shutil.move(src_path, dst_path)
            print(f"Moved {file} to {folder}/")
        

    
  








# iterate through that file list matching names with file names




