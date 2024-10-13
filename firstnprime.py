def is_prime(num):
    if num <= 1:
        return False

    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    return flag

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Enter the number of prime numbers you want: "))
print(first_n_primes(n))
