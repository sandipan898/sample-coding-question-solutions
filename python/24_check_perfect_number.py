def check_proper_divisor(number):
    divisors = list()
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number(number):
    perfect_number = 0
    divisors = check_proper_divisor(number)
    for i in range(len(divisors)):
        perfect_number += divisors[i]

    return perfect_number == number

num = 6
# num = 15
# num = 28
# num = 8128
if is_perfect_number(num):
    print("{} is a Perfect Number".format(num))
else:
    print("{} is not a Perfect Number".format(num))
