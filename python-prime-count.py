# python-prime-count.py

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

if __name__ == "__main__":
    N = 10000
    total_primes = count_primes(N)
    print(f"Number of primes up to {N}: {total_primes}")
