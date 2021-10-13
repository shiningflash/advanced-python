def prime_factors(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if N % divisor == 0:
            factors.append(divisor)
            N /= divisor
        else:
            divisor += 1
    return factors

if __name__=='__main__':
    N = 100
    print(prime_factors(N))