def find_digits(number):
    digits = list()
    while number > 0:
        digits.append(number%10)
        number = int(number/10)
    return digits

def check_same_ending(square, number):
    digits_sq = find_digits(square)
    digits_num = find_digits(number)
    # for i in reversed(range(len(digits_num))):
    for i in range(len(digits_num)-1, 0, -1):
        if digits_sq[i] != digits_num[i]:
            return False
    return True

def is_automorphic_number(number):
    square = number ** 2
    return check_same_ending(square, number)

# num = 6
# num = 25
num = 76
# num = 19

if is_automorphic_number(num):
    print("{} is an Automorphic Number".format(num))
else:
    print("{} is not an Automorphic Number".format(num))
