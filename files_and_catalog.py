import os.path
import shutil


# задание 4.1.
def files_and_catalog(dir, ext, Flag):
    files = []
    dirs = [] 
    for f in os.listdir(dir):
        if os.path.isdir(os.path.join(dir,f)):
            dirs.append(f)
        else:
            if ext == ".*" or f.endswith(ext):
                files.append(f)

    if (Flag):
       f1 = []
       d1 = []
       for d in dirs: 
           res = files_and_catalog(os.path.join(dir,d), ext, False)
           f1.extend(res[0])
           d1.extend(res[1])           

       files.extend(f1)
       dirs.extend(d1)           

    return [files, dirs]
                
# задание 4.2.
def delite(dir):
    if not os.path.isdir(dir):
        return
    
    all_in_dir = os.listdir(dir)

    for f in all_in_dir:
        if os.path.isdir(f):
            return False
        
    shutil.rmtree(dir)
    return True
