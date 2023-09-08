# Learning: Adição versus Incrementar

# Libraries
import time


# Functions
def addition_test(loop):
    """
    Performs a n loop times addition function to check the time to
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


def incr_test(loop):
    """
    Performs a n loop times addition function to check the time to
    execute it.

    """
    i = 0
    buffer = []

    time_in = time.time()
    while(i <= loop):
        buffer.append(1)
        i += 1

    time_out = time.time()
    duration = time_out - time_in

    return duration


# Main Program ---------------------------------------------------------
print("\n ****  Comparativo das funções Adição e Incrementar  **** \n")

limit = 100000
loop = 50
print(f" > Número de Interações = {limit}")
print(f" > Número de loop = {loop} \n")

# Generate times
sample_add, sample_incr, sample_faster = [], [], []

t = 0
while(t < loop):
    # Função Addition
    time_add = addition_test(limit)
    sample_add.append(time_add)

    # Função Incr
    time_incr = incr_test(limit)
    sample_incr.append(time_incr)
    
    faster = time_add/time_incr
    sample_faster.append(faster)
    print(f" > [{t+1}] A função append foi {faster:.3f} vezes mais rápida.")

    t = t+1


# Calculate mean
add_mean = sum(sample_add) / len(sample_add)
incr_mean = sum(sample_incr) / len(sample_incr)
faster_mean = sum(sample_faster) / len(sample_faster)

print(f"\n > O tempo médio de processamento da função 'i = i+1' foi {add_mean:.3f}")
print(f" > O tempo médio de processamento da função 'i += 1' foi {incr_mean:.3f}")
print(f" > A função append foi {faster_mean:.4f} vezes mais rápida que a função '+[]'\n")

