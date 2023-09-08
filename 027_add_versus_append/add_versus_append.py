# Learning: Append versus + []

# Libraries
import time


# Functions
def add_test(loop):
    """
    Performs a n loop times addition function to check the time to
    execute it.

    """
    i = 0
    buffer = []

    time_in = time.time()
    while(i <= loop):
        buffer = buffer + [1]
        i = i+1

    time_out = time.time()
    duration = time_out - time_in

    return duration


def append_test(loop):
    """
    Performns a n loop times append function to check the time to
    execute it.

    """
    i = 0
    buffer = []

    time_in = time.time()
    while(i <= loop):
        buffer.append(1)
        i = i+1

    time_out = time.time()
    duration = time_out - time_in

    return duration

    

# MAIN Program ----------------------------------------------------------
print("\n ****  Comparativo das funções Adição de Lista e Append  **** \n")

limit = 25000
loop = 2000
print(f" > Número de Interações = {limit}")
print(f" > Número de loop = {loop} \n")

# Generate times
sample_add, sample_append, sample_faster = [], [], []

t = 0
while(t < loop):
    # Função Add
    time_add = add_test(limit)
    sample_add = sample_add + [time_add]    # :)

    # Função Append
    time_append = append_test(limit)
    sample_append.append(time_append)
    
    faster = time_add/time_append
    sample_faster.append(faster)
    print(f" > [{t+1}] A função append foi {faster:.3f} vezes mais rápida.")

    t = t+1

# Calculate mean
add_mean = sum(sample_add) / len(sample_add)
append_mean = sum(sample_append) / len(sample_append)
faster_mean = sum(sample_faster) / len(sample_faster)

print(f"\n > O tempo médio de processamento da função '+[]' foi {add_mean:.3f}")
print(f" > O tempo médio de processamento da função .append foi {append_mean:.3f}")
print(f" > A função append foi {faster_mean:.4f} vezes mais rápida que a função '+[]'\n")

