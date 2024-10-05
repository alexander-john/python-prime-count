# Prime count analysis!
### Parallelization

Parallelization is a computer science technique that divides large computational tasks into smaller sub-tasks to be executed simultaneously on multiple processors or cores. The goal of parallelization is to reduce the overall computation time and process large volumes of data more efficiently and faster. 

Here is our parallelization code.

```python
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
```

Using `cProfile` we get the following performance improvements!

```bash
python3 -m cProfile -s cumtime python-prime-count.py
```

```bash
21170 function calls (20882 primitive calls) in 0.091 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     32/1    0.000    0.000    0.091    0.091 {built-in method builtins.exec}
        1    0.000    0.000    0.091    0.091 python-prime-count.py:3(<module>)
        1    0.000    0.000    0.075    0.075 python-prime-count.py:13(count_primes_parallel)
        1    0.000    0.000    0.045    0.045 context.py:115(Pool)
     55/6    0.000    0.000    0.033    0.005 <frozen importlib._bootstrap>:1002(_find_and_load)
     55/6    0.000    0.000    0.032    0.005 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
        1    0.000    0.000    0.032    0.032 pool.py:183(__init__)
     50/6    0.000    0.000    0.032    0.005 <frozen importlib._bootstrap>:659(_load_unlocked)
        .
        .
        .
```

<img width="927" alt="Screen Shot 2024-10-04 at 5 47 25 PM" src="https://github.com/user-attachments/assets/d99b4e66-7078-4435-9357-cbe415433543">

We reduced execution time by 4x! That is all the ideas I have. Let's conclude this mess with a recap.

## Conclusion

Switch to the `re-cap` branch to see the conclusion.

