def writeToFile(filename,l):
    file = open(filename, 'a')
    file.write(str(l))
    file.close()

    file = open(filename, 'r')
    print(file.read())
