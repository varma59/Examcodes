def pthFactor(n, p):
    factors = []
    sqrt_n = int(math.sqrt(n))

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)
    
    if p <= len(factors):
        return factors[p - 1]
    
    elif p <= 2 * len(factors) - (1 if sqrt_n * sqrt_n == n else 0):
        return n // factors[-(p - len(factors) + (1 if sqrt_n * sqrt_n == n else 0))]
    
    else:
        return 0
