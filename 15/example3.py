def decorator(func):
    def wrapper(*args, **kwargs):
        print("executando antes da funcao...")
        func(*args, **kwargs)
        print("executando depois da funcao...")
    return wrapper

@decorator
def get_name(name):

    print(f"Executando funcao com o argumento {name}")

if __name__ == "__main__":
    
    name = "PythonTrap"
    get_name(name)