# python-prime-count.py

import math

def count_primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*2:n+1:current] = [False] * len(range(current*2, n+1, current))
    return sum(sieve)

if __name__ == "__main__":
    N = 10000
    total_primes = count_primes_sieve(N)
    print(f"Number of primes up to {N}: {total_primes}")
