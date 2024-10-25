import os

def find_file(way: str = '.') -> list:
    directory = os.listdir(way)
    file_in_directory = directory[:]

    if file in directory:
        path_file = way + '/' + file
        isfile = os.path.isdir(path_file)

        new_directory = []
        if isfile:
            new_directory = find_file(path_file)

        file_in_directory.extend(new_directory)

    return file_in_directory