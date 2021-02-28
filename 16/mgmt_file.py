import os

def create_file():

    path = os.getcwd() + "/16"
    file_name = "pythontrap.txt"

    #creating and write file.
    with open(os.path.join(path, file_name), "w") as fl:
        fl.write("16 tips python trap")
        fl.close()
    
    # print before rename
    print(os.listdir(path))

    #rename file
    os.rename(
        os.path.join(path, file_name),
        os.path.join(path, "rename_pythontrap.txt")
    )

    # print after rename
    print(os.listdir(path))

if __name__ == "__main__":

    create_file()