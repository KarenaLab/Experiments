
import math

def next_prime(number):
    """


    """
    if(number < 0):
        raise ValueError("Negative numbers cannot be primes")

    # Base case
    if(number <= 1):
        return 2

    # Case
    # IF the number is even, decrease one (and odd)
    if(number % 2 == 0):
        number = number - 1


    while(True):
        # Check only odd numbers, because even numbers are divisible per 2.
        number = number + 2

        # Only need to check up to and including square root value.
        max_check = int(math.sqrt(number)) + 2

        for divider in range(3, max_check, 2):
            # If the division of number per divider is "perfect", number
            # is not prime.
            if(number % divider == 0):
                break

        else:
            return number



limit = 1000
number = 1

while(number < limit):
    number = next_prime(number)
    print(number)
    

    




                
