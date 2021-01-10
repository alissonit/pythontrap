import sys

try:
    f = open('file2.txt')
    s = f.readline()
    i = int(s.strip())
    print(f"number: {i}")
except ValueError:
    raise ValueError("Only numbers are allowed")
except FileNotFoundError as err:
    print(f"File NotFound error: {err}")
except:
    print("Unexpected error:", sys.exc_info()[0])