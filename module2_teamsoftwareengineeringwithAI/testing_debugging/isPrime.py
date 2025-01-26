import time
import cProfile
import pstats

def is_prime(n):
    """
    Check if 'n' is a prime number.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def sum_of_primes_in_list(numbers):
    """
    Calculate the sum of prime numbers in the list of integers 'numbers'.
    """
    total = 0
    for num in numbers:
        if is_prime(num):
            total += num
    return total

if __name__ == "__main__":
    # Create a list of numbers from 1 to 100000
    num_list = list(range(1, 100001))

    # Start timing
    start_time = time.time()
    
    # Profiling the function
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = sum_of_primes_in_list(num_list)
    
    profiler.disable()
    end_time = time.time()

    # Display profiling results
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(10)  # Show top 10 time-consuming functions

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    print(f"The sum of prime numbers from 1 to 100000 is {result}.")
    print(f"Calculation took {elapsed_time:.2f} seconds.")
