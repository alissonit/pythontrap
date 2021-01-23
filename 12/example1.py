# WITHOUT GENERATORS
import get_mem
import time

print(f"Memory (Before): {get_mem.memory_usage_psutil()}Mb")
def mult_num(num):
    list_num = []
    for n in range(num):
        value = {
            'old_num': n,
            'new_num': n*n
        }
        list_num.append(value)
    return list_num

start_time = time.time()
resp = mult_num(3000000)

print(type(resp))

print(f"Memory (After): {get_mem.memory_usage_psutil()}Mb", end="\n\n")
print(f"--- {(time.time() - start_time)} seconds ---")
