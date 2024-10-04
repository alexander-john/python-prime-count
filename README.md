# Prime count analysis!
## Sieve of Eratosthenes

In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.

It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime. This is the sieve's key distinction from using trial division to sequentially test each candidate number for divisibility by each prime. Once all the multiples of each discovered prime have been marked as composites, the remaining unmarked numbers are primes.

Here is our Sieve of Eratosthenes algorithm.

```python
def count_primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*2:n+1:current] = [False] * len(range(current*2, n+1, current))
    return sum(sieve)
```

Using `cProfile` we get the following performance improvements!

```bash
python3 -m cProfile -s cumtime python-prime-count.py
```

```bash
241 function calls in 0.001 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.001    0.001 python-prime-count.py:3(<module>)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:558(module_from_spec)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        .
        .
        .
```
<img width="927" alt="Screen Shot 2024-10-04 at 4 18 11 PM" src="https://github.com/user-attachments/assets/7f092efb-c792-43fe-9ddb-381f80860843">

We reduced execution time by 17x! Lets not stop here, I have a better idea!

## Utilizing NumPy

Switch to the `num-py` branch to see the NumPy optimization.

