def calculate_factorial(number):
    if number in [0, 1]:
        return 1
    return number*calculate_factorial(number-1)

def is_strong_number(number):
    num = number
    strong_number = 0
    while number > 0:
        strong_number += calculate_factorial(number%10)
        number = int(number/10)
    return strong_number == num

# num = 145
num = 40585
if is_strong_number(num):
    print("{} is a Strong Number".format(num))
else:
    print("{} is not a Strong Number".format(num))
