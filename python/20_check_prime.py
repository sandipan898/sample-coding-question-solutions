def is_prime(number):
    for i in range(2, number/2):
        return number % i == 0
        