def power_of_number(number, power):
    # return number ** power
    for i in range(1, power):
        number *= number
    return number

num = 8
pow = 2
print("Power of {} is {}".format(num, power_of_number(num, pow)))