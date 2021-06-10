def is_prime(number):
    for i in range(2, int(number/2)):
        if number % i == 0:
            return False
    return True

# num = 21
num = 59
if is_prime(num):
    print("{} is a Prime Number".format(num))
else:
    print("{} is not a Prime Number".format(num))
