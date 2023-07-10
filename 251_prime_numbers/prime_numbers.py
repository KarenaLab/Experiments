
def prime_numbers(limit, verbose=False):
    """
    Separates a list of prime numbers from 1 to the limit informed.
    Returns: list of prime numbers and time to process.
    
    """
    import time

    prime_list = []
    time_in = time.time()
    for number in range(1, limit+1):
        div = 0
        for i in range(1, number+1):
            if(number % i == 0):
                div = div+1

            if(div > 2):
                break
            
        if(div == 2):
            prime_list.append(number)
            if(verbose == True):
                print(f" > {number} is prime number")


    time_out = time.time()
    time_delta = time_out - time_in
    
    return prime_list, time_delta

