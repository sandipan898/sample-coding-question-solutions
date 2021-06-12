def reverse_number(number):
    sum = 0
    while number > 0:
        rem = number % 10
        sum = sum * 10 + rem
        number = number // 10
    return sum 

def replace_zeros(number):
    sum = 0
    while number > 0:
        rem = number % 10
        number = number // 10
        if rem == 0:
            rem = 1
        sum = sum * 10 + rem
    return reverse_number(sum)

# num = 1100101
# num = 122012010
num = 1201
print("Number {} after replacing all  0s with 1: {}".format(num, replace_zeros(num)))
