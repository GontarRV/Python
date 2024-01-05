import os.path
import glob
import shutil


# задание 4.1.
def files_and_catalog(dir, expan, Flag):
    if not os.path.isdir(dir):
        return
    
    if Flag:
        all_in_dir = os.listdir(dir)

        for f in all_in_dir:
            dir1 = os.path.join(dir, f)
            print(dir1)

            if os.path.isdir(dir1):
                files_and_catalog(dir1, expan, Flag)
            else:
                print(glob.glob(expan))

    else:
        print(glob.glob(expan))
        all_in_dir = os.listdir(dir)

        for f in all_in_dir:
            dir1 = os.path.join(dir, f)
            if os.path.isdir(dir1):
                print(dir1)
                
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
