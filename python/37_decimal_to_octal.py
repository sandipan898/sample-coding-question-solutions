def decimal_to_octal(number):
    sum = 0
    power = 0
    while number > 0:
        rem = number % 8
        sum += (10**power)*rem 
        number = number // 8
        power += 1
    return sum

# num = 32
# num = 16
# num = 33
num = 8
print("The Octal representation of {} is: {}".format(num, decimal_to_octal(num)))
