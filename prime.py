def get_divisors(n):
    divisors = []  # to store divisors
    for i in range(2, n):  # check all numbers from 2 to n-1
        if n % i == 0:
            divisors.append(i)  # add the divisor to the list
    return divisors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # if n is divisible by i, it's not prime
            return False
    return True  # if no divisors found, it's prime

x = int(input("number: "))

if x <= 0:
    print(f"{x} is lunchly (i like my cheese drippy bruh) but its taken :((((((((")
elif is_prime(x):
    print(f"{x} is prime and single 💀")
else:
    divisors = get_divisors(x)
    print(f"{x} is lunchly (i like my cheese drippy bruh) and its lovers are: {divisors}")

input("\npress enter to exit...")
