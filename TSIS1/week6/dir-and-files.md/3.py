import os
def find_file_and_directory(p):
    if os.path.exists(path=p):
        file_name = os.path.basename(path=p)
        directory = os.path.dirname(path=p)
        return (file_name, directory)
    else:
        print(f"The path '{p}' does not exist.")
