# python-prime-count.py

import math

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


if __name__ == "__main__":
    N = 10000
    total_primes = count_primes_sqrt(N)
    print(f"Number of primes up to {N}: {total_primes}")
