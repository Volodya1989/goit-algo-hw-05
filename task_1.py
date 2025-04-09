
def caching_fibonacci():
    #  cache previously used for Fibonacci numbers
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # return if cache available
        if n in cache:
            return cache[n]
        # calculated and stored in the cache
        cache[n] = fibonacci(n-1)+fibonacci(n-2)
        return cache[n]
    return fibonacci


fib = caching_fibonacci()
print(fib(15))
