def octal_to_decimal(number):
    sum = 0
    power = 0
    while number > 0:
        rem = number % 10
        sum += (8**power)*rem
        power += 1
        number = number // 10
    return sum

# num = 67 # 55
num = 512 # 330
print("The Decimal representation of the Octal number {} is: {}".format(num, octal_to_decimal(num)))
