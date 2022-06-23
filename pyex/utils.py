import os

def get_filename_without_extension(filepath):
    return ".".join(os.path.basename(filepath).split(".")[:-1])

def change_extension(filepath, new_extension):
    return ".".join([get_filename_without_extension(filepath),new_extension])

def is_file_of_extension(filepath, extension):
    return not os.path.isdir(filepath) and filepath.endswith("."+extension)