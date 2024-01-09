from zipfile import ZipFile
import os

def zip_archive(name, ext):
    path = os.getcwd()
    name_with_ext = name + '.zip'
    files = []
    for file in os.listdir(path):
        if ext == ".*" or file.endswith(ext):
            files.append(file)
    
    if len(files) == 0:
        return

    with ZipFile(name_with_ext, "w") as fil:
        for file in files:
            fil.write(file)
