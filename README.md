# Prime count analysis!
## Original program

Using `cProfile` we see that `count_primes` is consuming the most time.

```bash
python3 -m cProfile -s cumtime python-prime-count.py
```

```
5 function calls in 0.397 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.397    0.397 {built-in method builtins.exec}
        1    0.000    0.000    0.397    0.397 python-prime-count.py:3(<module>)
        1    0.397    0.397    0.397    0.397 python-prime-count.py:3(count_primes)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

<img width="899" alt="Screen Shot 2024-10-03 at 10 55 52 AM" src="https://github.com/user-attachments/assets/655039c9-c6a0-4b39-80ac-3ae1638345b9">

Looking at `count_primes` we see that the outer loop iterates from `2` to `n + 1` and the inner loop checks if the current number is divisible by any number less than itself.

```python
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
```

This is pretty much a brute-force method and is very inefficient.

## Lets optimize!
### Optimize inner loop

After modifying `count_primes` we end up with the following program. 

```python
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
```

The idea here is that there is no need to check every number less than `num` from `count_primes`. We can check up to the square root, becuase if a number has a factor larger than its square root, it must be paired with a factor smaller than the square root. If no factors are found up to the square root, the number cannot have any other factors, and thus it is prime. Thus, we reduce the number of iterations in the inner loop, leading to an improved execution.

Using `cProfile` we get the following performance improvements!

```bash
python3 -m cProfile -s cumtime python-prime-count.py
```

```
10214 function calls in 0.017 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
        1    0.000    0.000    0.017    0.017 python-prime-count.py:3(<module>)
        1    0.013    0.013    0.014    0.014 python-prime-count.py:5(count_primes_sqrt)
        1    0.000    0.000    0.003    0.003 <frozen importlib._bootstrap>:1002(_find_and_load)
        1    0.000    0.000    0.003    0.003 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
        1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:659(_load_unlocked)
        2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:558(module_from_spec)
```

<img width="899" alt="Screen Shot 2024-10-04 at 12 03 29 PM" src="https://github.com/user-attachments/assets/20ba44b7-2fb1-47fc-8416-ab47ade52cb6">

We reduced execution time by 95.72%. Lets not stop here, I have a better idea!

## Sieve of Eratosthenes

Switch to the `sieve-of-eratosthenes` branch to see the Sieve of Eratosthenes optimization.


