# python-prime-count.py

import numpy as np

def count_primes_numpy(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*2::current] = False
    return np.sum(sieve)

if __name__ == "__main__":
    N = 10000
    total_primes = count_primes_numpy(N)
    print(f"Number of primes up to {N}: {total_primes}")
