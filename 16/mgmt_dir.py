import os

def create_dir():
    # Directory name  
    dir_name = "createFromPython"
    # Parent Directory path  
    parent_dir = os.getcwd() + "/16"
    # path 
    path = os.path.join(parent_dir, dir_name)
    # create DIR
    try:
        os.mkdir(path, mode=0o755)
        print(f"Directory {dir_name} created!")
    except FileExistsError:
        print(f"Directory {dir_name} already exists!")
    
    return path

def create_sub_dir(path):

    sub_dir = "createFromMakeDir"

    new_path = path + "/sub/" + sub_dir

    # create a directory recursively
    os.makedirs(new_path, mode=0o755)

    # output list directory
    print(os.listdir(path=path))

def remove_dir(path):

    try:
        rm_dir = os.rmdir(path)
    except (OSError, FileNotFoundError):
        print(f"removing all in dir {path}")
        # Use os system to execute shell command
        os.system(f"rm -rf {path}/*")
        print(f"removing dir: {path}")
        rm_dir = os.rmdir(path)

    return rm_dir

if __name__ == "__main__":

    path = create_dir()

    create_sub_dir(path)

    remove_dir(path)
    