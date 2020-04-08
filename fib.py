def fib(n):
    """returns the nth fibonacci number"""
    fibs = [0, 1]
    count = 0
    while len(fibs) <= n:
        a = fibs[count] + fibs[count + 1]
        fibs.append(a)
        count += 1

    return fibs[n]
