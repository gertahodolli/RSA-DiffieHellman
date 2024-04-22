from matplotlib import pyplot as plt

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result *= (1.0 - (1.0 / p))
        p += 1
    if n > 1:
        result *= (1.0 - (1.0 / n))
    return int(result)

list_n = []
list_phi_n = []

for n in range(1, 10000):
    list_n.append(n)
    list_phi_n.append(phi(n))

# Print results in the console
for n, phi_n in zip(list_n, list_phi_n):
    print(f"phi({n}) = {phi_n}")

plt.scatter(list_n, list_phi_n, label='EulerPhi', color='k', marker='.', s=10)

plt.xlabel('n')
plt.ylabel('Phi(n)')
plt.title('Graph plot of Euler Phi function')
plt.legend()
plt.grid(True)
plt.show()