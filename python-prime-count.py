# python-prime-count.py

from multiprocessing import Pool

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
    total_primes = count_primes_parallel(N)
    print(f"Number of primes up to {N}: {total_primes}")
