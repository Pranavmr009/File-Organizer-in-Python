import os
from pathlib import Path
import shutil
import datetime
import hashlib

found_extensions = []

def create_folders(path):
    for extension in found_extensions:
        folder_name = extension[1:]
        full_path = os.path.join(path, folder_name)

        if extension != '.py' and not os.path.exists(folder_name): 
            os.mkdir(full_path)


def sort_according_to_file_types(path):
    global found_extensions
    found_extensions = []

    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            extension =Path(file).suffix
            if extension and extension not in found_extensions and extension!= '.py':
                found_extensions.append(extension)
            
    create_folders(path)
            
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            extension = Path(file).suffix
            if extension and extension in found_extensions and extension != '.py':
                folder_name = extension[1:]
                folder_path = os.path.join(path, folder_name)
                shutil.move(full_path, os.path.join(folder_path, file))


def sort_according_to_date_modified(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and Path(file).suffix != '.py':
            last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
            year = str(last_modified_time.year)
            month = str(last_modified_time.strftime("%B"))

            destination_folder = os.path.join(path, year, month)
            os.makedirs(destination_folder, exist_ok=True)

            shutil.move(full_path, os.path.join(destination_folder, file))


def find_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
        
    return hasher.hexdigest()

def find_duplicates(path):
    hash_dict = {}
    duplicates = []
    deleted = []


    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            file_hash = find_hash(full_path)
            if file_hash in hash_dict:
                duplicates.append(file)
            else:
                hash_dict[file_hash] = file
    
    # while True:
    #     delete_or_move = input("Would you like to move or delete duplicate files (D = delete or M = move): ")
    if duplicates:
        duplicates_folder = os.path.join(path, "Duplicates")
        os.makedirs(duplicates_folder, exist_ok=True)

        for duplicate in duplicates:
            shutil.move(duplicate, os.path.join(duplicates_folder, os.path.basename(duplicate)))
        print(f"Moved {len(duplicates)} duplicate files to {duplicates_folder}")

    else:
        print("No duplicates found")

    

# sort_according_to_file_types(".")

# sort_according_to_date_modified(".")

# find_duplicates(".")


