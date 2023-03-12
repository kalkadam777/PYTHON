import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} has been deleted.")
        else:
            print(f"{path} cannot be deleted: permission denied.")
    else:
        print(f"{path} does not exist.")