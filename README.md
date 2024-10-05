# Prime count analysis!
### NumPy!

NumPy targets the CPython reference implementation of Python, which is a non-optimizing bytecode interpreter. Mathematical algorithms written for this version of Python often run much slower than compiled equivalents due to the absence of compiler optimization. NumPy addresses the slowness problem partly by providing multidimensional arrays and functions and operators that operate efficiently on arrays; using these requires rewriting some code, mostly inner loops, using NumPy.

Here is our NumPy optimization.

```python
def count_primes_numpy(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*2::current] = False
    return np.sum(sieve)
```

Using `cProfile` we get the following performance improvements!

```bash
python3 -m cProfile -s cumtime python-prime-count.py
```

```bash
75310 function calls (73044 primitive calls) in 0.115 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        8    0.001    0.000    0.273    0.034 __init__.py:1(<module>)
     94/1    0.000    0.000    0.115    0.115 {built-in method builtins.exec}
        1    0.000    0.000    0.115    0.115 python-prime-count.py:3(<module>)
    112/1    0.001    0.000    0.114    0.114 <frozen importlib._bootstrap>:1002(_find_and_load)
    112/1    0.000    0.000    0.114    0.114 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
    106/1    0.001    0.000    0.114    0.114 <frozen importlib._bootstrap>:659(_load_unlocked)
     93/1    0.000    0.000    0.114    0.114 <frozen importlib._bootstrap_external>:784(exec_module)
    164/1    0.000    0.000    0.114    0.114 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
        .
        .
        .
```

<img width="927" alt="Screen Shot 2024-10-04 at 5 33 38 PM" src="https://github.com/user-attachments/assets/32a8cd03-ccc4-43b6-b2ba-a6da8dc1e455">

We got a 3x improvement. Not quite the 397x improvement we got with the Sieve of Eratosthenes optimization but an improvement nonetheless. I have one more idea!

## Parallelization!

Switch to the `Parallelization` branch to see the Parallelization optimization.
