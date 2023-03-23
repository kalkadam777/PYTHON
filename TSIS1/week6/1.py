from string import ascii_uppercase
def generate_files():
    for ch in ascii_uppercase:
        file=open(f"{ch}.py",'x')
        file.close()
    print("files 1-6")
generate_files()