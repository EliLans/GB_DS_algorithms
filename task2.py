### 2. Написать два алгоритма нахождения i-го по счёту простого числа.

import cProfile as cp
import math, sys

n = int(input('Введите порядковый номер простого числа: '))


### Без использования «Решета Эратосфена»;

def algo(n):
    primes = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(f'Искомое простое число = {primes[n - 1]} (БЕЗ РЕШЕТА)')


cp.run('algo(n)')

# Введите порядковый номер простого числа: 1000
# Искомое простое число = 7919 (БЕЗ РЕШЕТА)
#          1234 function calls in 1.557 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.557    1.557 <string>:1(<module>)
#         1    1.556    1.556    1.557    1.557 les04.py:68(algo)
#         1    0.000    0.000    1.557    1.557 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('======================================')


### Используя алгоритм «Решето Эратосфена»

def sieve(n):
    primes = []
    nums = [i for i in range(2, 10000)]

    for i in nums:
        if i != 0:
            primes.append(i)
            for j in nums[i:]:
                if j % i == 0:
                    nums[j - 2] = 0
    print(f'Искомое простое число = {primes[n - 1]} (РЕШЕТО)')


cp.run('sieve(n)')

# Введите порядковый номер простого числа: 1000
# Искомое простое число = 7919 (РЕШЕТО)
#               1236 function calls in 2.092 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.092    2.092 <string>:1(<module>)
#         1    2.082    2.082    2.091    2.091 les04.py:97(sieve)
#         1    0.001    0.001    0.001    0.001 les04.py:99(<listcomp>)
#         1    0.000    0.000    2.092    2.092 {built-in method builtins.exec}
#         2    0.007    0.004    0.007    0.004 {built-in method builtins.print}
#      1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}