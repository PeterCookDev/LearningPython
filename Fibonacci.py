

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

known = {0:0,1:1}

def fibonacci_memoized(n):
    if n in known:
        return known[n]

    res = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    known[n] = res
    return res

print(fibonacci(10))
print(fibonacci_memoized(10))
