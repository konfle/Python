# Lesson 4 - optimization with Cache
import time
import functools


@functools.lru_cache()
def factorial(n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


start = time.time()
for i in range(1, 11):
    print('{}! {}'.format(i, factorial(i)))
stop = time.time()
print('Execution time', stop - start)

print(factorial.cache_info())

'''
start = time.time()
for i in range(1, 11):
    print('{}! {}'.format(i, factorial(i)))
stop = time.time()
print('Execution time', stop - start)
'''

# LAB


@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(1, 37):
    time_now = time.time()
    fib(i)
    print('fib iteration {} time difference {}'.format(i, time_now - start))
end = time.time()
fib_time = end - start
print('Execute time:', fib_time)

print(fib.cache_info())
