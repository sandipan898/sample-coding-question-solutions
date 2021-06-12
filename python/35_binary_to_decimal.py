def binary_to_decimal(number):
    power = 0
    sum = 0
    while number > 0:
        rem = number % 10
        sum += (2**power)*rem
        number = number // 10
        power += 1
    return sum

# num = 1011
# num = 101101
num = 111
print("The Decimal representation of {} is: {}".format(num, binary_to_decimal(num)))
