def generate_files():
    for ch in ascii_uppercase:
        file=open(f"./files/{ch}.txt",'x')
        file.close()
    print("files A-Z")
