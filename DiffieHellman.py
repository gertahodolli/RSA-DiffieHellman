import random


# Function to calculate Euler's totient function
def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result *= (1.0 - (1.0 / p))
        p += 1
    if n > 1:
        result *= (1.0 - (1.0 / n))
    return int(result)


# Function to calculate modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result


# Diffie-Hellman Key Exchange with Euler's phi function
def diffie_hellman_phi():
    # Input prime number and generator
    prime = int(input("Enter prime number: "))

    # Calculate Euler's phi function for p
    phi_p = euler_phi(prime)

    # Choose a primitive root modulo p
    candidate_primitives = [i for i in range(2, prime) if pow(i, phi_p, prime) == 1]
    if not candidate_primitives:
        print("No primitive root found for the given prime.")
        return None, None
    generator = random.choice(candidate_primitives)
    print("Chosen generator:", generator)

    # Input Alice's private key
    a_private = int(input("Enter Alice's private key: "))
    # Input Bob's private key
    b_private = int(input("Enter Bob's private key: "))
    # Calculate public keys
    a_public = mod_exp(generator, a_private, prime)
    b_public = mod_exp(generator, b_private, prime)

    # Shared secret calculation
    alice_secret = mod_exp(b_public, a_private, prime)
    bob_secret = mod_exp(a_public, b_private, prime)

    # Both should have the same shared secret
    return alice_secret, bob_secret


# Main function
def main():
    alice_secret, bob_secret = diffie_hellman_phi()
    if alice_secret is not None and bob_secret is not None:
        # Output shared secrets
        print("Alice's shared secret:", alice_secret)
        print("Bob's shared secret:", bob_secret)


# Run the main function
if __name__ == "__main__":
    main()