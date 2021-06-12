def binary_to_decimal(number):
    sum = 0
    power = 0
    while number > 0:
        rem = number % 10
        sum += (2**power)*rem
        number = number // 10
        power += 1
    return sum

def decimal_to_octal(number):
    sum = 0
    power = 0
    while number > 0:
        rem = number % 8
        sum += (10**power)*rem
        number = number // 8
        power += 1
    return sum

def binary_to_octal(number):
    decimal_number = binary_to_decimal(number)
    return decimal_to_octal(decimal_number)

# num = 1100101 # 145
# num = 110001110 # 616
num = 1000 # 10
print("The Octal representation of the Binary number {} is: {}".format(num, binary_to_octal(num)))
