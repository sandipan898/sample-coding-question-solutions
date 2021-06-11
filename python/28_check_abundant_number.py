def find_proper_divisors(number):
    divisors = list()
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def is_abundant_number(number):
    sum = 0
    proper_divisors = find_proper_divisors(number)
    for divisor in proper_divisors:
        sum += divisor
    return sum > number 

# num = 12
# num = 18
num = 21
if is_abundant_number(num):
    print("{} is an Abundant NUmber".format(num))
else:
    print("{} is not an Abundant NUmber".format(num))
