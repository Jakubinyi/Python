def fibonacci(n):
    cache = [0, 1]
    for i in range(n):
        cache_length = len(cache)
        result = cache[cache_length - 1] + cache[cache_length - 2]
        cache.append(result)
    return cache
print(fibonacci(5))