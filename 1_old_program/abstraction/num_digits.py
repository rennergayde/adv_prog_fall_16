def counter(n):
    if n < 10:
        return 1
    else:
        return 1 + counter(n/10)
