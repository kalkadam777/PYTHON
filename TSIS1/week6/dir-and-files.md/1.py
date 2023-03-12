import os
def listDirs(p):
    directories = []
    for x in os.scandir(path=p):
        if x.is_dir():
            directories.append(x.name)
    print(directories)
def listFiles(p):
    directories1=[]
    for x in os.scandir(path=p):
        if x.is_file():
            directories1.append(x.name)
def listDirsAndFiles(p):
    files_and_dirs = []
    for x in os.scandir(path=p):
        files_and_dirs.append(x.name)
    print(files_and_dirs)