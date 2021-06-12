def is_prime(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True

def prime_in_range(lower, upper):
    prime_numbers = list()
    for number in range(lower, upper+1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

upper = 100
lower = 12
prime_numbers = prime_in_range(lower, upper)
for prime in prime_numbers:
    print(prime)