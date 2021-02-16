def decorator(func):
    def wrapper():
        print("executando antes da funcao...")
        func()
        print("executando depois da funcao...")
    return wrapper

def get_name():

    print(f"Executando funcao")

if __name__ == "__main__":

    function_decorated = decorator(get_name)

    function_decorated()