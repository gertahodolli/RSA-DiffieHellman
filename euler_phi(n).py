def euler_phi(n):
    result = n  # Initialize result as n

    # Consider all prime factors of n and subtract their multiples
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result *= (1.0 - (1.0 / p))
        p += 1

    # If n has a prime factor greater than sqrt(n), subtract its multiple
    if n > 1:
        result *= (1.0 - (1.0 / n))

    return int(result)

def main():
    n = int(input("Enter a number: "))
    print("Euler's Totient Function value of", n, "is:", euler_phi(n))

if __name__ == "__main__":
    main()