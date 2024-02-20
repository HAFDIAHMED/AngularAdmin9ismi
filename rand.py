import math

# Function to check if n is prime or not
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if i * i <= n and n % i == 0:
            return False
    return True

# Function to calculate the Möbius function for a positive integer
def mobius(N):
    # Base Case
    if N == 1:
        return 1

    # For a prime factor i, check if i^2 is also a factor.
    p = 0
    for i in range(1, N + 1):
        if N % i == 0 and isPrime(i):
            # Check if N is divisible by i^2
            if N % (i * i) == 0:
                return 0
            else:
                # i occurs only once, increase p
                p += 1

    # All prime factors are contained only once.
    # Return 1 if p is even, else -1
    return -1 if p % 2 != 0 else 1

# Function to calculate Wn
def calculate_Wn(W0, n):
    result = W0
    for i in range(1, n + 1):
        result += (math.log(i)) * mobius(i) * math.pi
    return result

# Example usage:
W0 = 1  # Your initial value for W0
n = 100  # Your value for n
result = calculate_Wn(W0, n)
L=[]
for i in range(n):
    L.append(calculate_Wn(W0,i))
    # print(calculate_Wn(W0,i))



# print(result)
# Check for duplicates in the list L
unique_set = set()
duplicates_found = False

for i in L:
    if i in unique_set:
        print(f'Duplicate found: {i}')
        duplicates_found = True
    else:
        unique_set.add(i)

if not duplicates_found:
    print('No duplicates found.')
