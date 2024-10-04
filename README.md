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