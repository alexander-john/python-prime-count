# python-prime-count.py

import math, time
from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt

# time each function
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

# original
def count_primes(n):
    count = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

# inner loop
def count_primes_sqrt(n):
    count = 0
    for num in range(2, n + 1):
        is_prime = True
        sqrt_num = int(math.sqrt(num)) + 1
        for i in range(2, sqrt_num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

# Sieve
def count_primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*2:n+1:current] = [False] * len(range(current*2, n+1, current))
    return sum(sieve)

# NumPy
def count_primes_numpy(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*2::current] = False
    return np.sum(sieve)

# Parallelization
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_parallel(n):
    with Pool() as pool:
        return sum(pool.map(is_prime, range(2, n + 1)))

if __name__ == "__main__":
    N = 10000
    
    # Verify correctness
    total_primes_original = count_primes(N)
    total_primes_sqrt = count_primes_sqrt(N)
    total_primes_sieve = count_primes_sieve(N)
    total_primes_numpy = count_primes_numpy(N)
    total_primes_parallel = count_primes_parallel(N)
    
    assert total_primes_original == total_primes_sqrt == \
    total_primes_sieve == total_primes_numpy == \
    total_primes_parallel, "Results do not match!"
    print(f"Number of primes up to {N}: {total_primes_original}")
    
    # Measure performance
    result, duration = measure_time(count_primes, N)
    print(f"Brute-force method took {duration:.5f} seconds.")

    result, duration = measure_time(count_primes_sqrt, N)
    print(f"Square root method took {duration:.5f} seconds.")

    result, duration = measure_time(count_primes_sieve, N)
    print(f"Sieve of Eratosthenes took {duration:.5f} seconds.")
    
    result, duration = measure_time(count_primes_numpy, N)
    print(f"NumPy method took {duration:.5f} seconds.")

    result, duration = measure_time(count_primes_parallel, N)
    print(f"Parallelization method took {duration:.5f} seconds.")
    
    Ns = [10000, 100000]
    times_brute_force = [.4, 32]
    times_sqrt = [0.01, .18]
    times_sieve = [0.0004, 0.003]
    times_numpy = [0.0003, 0.0006]
    times_parallel = [1.2, 1.3]

    plt.figure(figsize=(10, 6))
    plt.loglog(Ns, times_brute_force, label='Brute-Force')
    plt.loglog(Ns, times_sqrt, label='Square Root Optimization')
    plt.loglog(Ns, times_sieve, label='Sieve of Eratosthenes')
    plt.loglog(Ns, times_numpy, label='NumPy Implementation')
    plt.loglog(Ns, times_parallel, label='Parallelization Implementation')
    plt.xlabel('N')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time vs N')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()
