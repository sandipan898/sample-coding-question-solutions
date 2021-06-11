def is_harshad_number(number):
    num = number
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number = int(number/10)
    return num % digit_sum == 0

# num = 21
# num = 11
num = 6804
if is_harshad_number(num):
    print("{} is a Harshad Number".format(num))
else:
    print("{} is not a Harshad Number".format(num))
