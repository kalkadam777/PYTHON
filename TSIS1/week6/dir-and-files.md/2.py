import os
def checkPath(p):


    exist_status = os.access(path = p, mode = os.F_OK)

    print(f"Existence: {exist_status}")

    read_status = os.access(path = p, mode = os.R_OK)

    print(f"Readibility: {read_status}")
 

    write_status = os.access(path = p, mode = os.W_OK)

    print(f"Writability: {write_status}")

    exec_status = os.access(path = p, mode = os.X_OK)

    print(f"Executability: {exec_status}")
