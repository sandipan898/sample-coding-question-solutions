def octal_to_decimal(number):
    decimal = 0
    power = 0
    while number > 0:
        rem = number % 10
        decimal += (8**power)*rem
        number = number // 10
        power += 1
    return decimal

def decimal_to_binary(number):
    binary = 0
    power = 0
    while number > 0:
        rem = number % 2
        binary += (10**power)*rem
        number = number // 2
        power += 1
    return binary

def octal_to_binary(number):
    decimal = octal_to_decimal(number)
    return decimal_to_binary(decimal)

# num = 10 # 1000
# num = 616 # 110001110
num = 345 # 011100101
print("The Binary representation of the Octal number {} is: {}".format(num, octal_to_binary(num)))
