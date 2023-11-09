from math import gcd

def coprimeCount(A):
    def is_coprime(a, b):
        return gcd(a, b) == 1

    B = []
    for a in A:
        count = sum(1 for i in range(1, a) if is_coprime(a, i))
        B.append(count)
    
    return B

# Example usage:
A = [5, 8, 14]
B = coprimeCount(A)
print(B)  # Output will be [4, 4, 6]
