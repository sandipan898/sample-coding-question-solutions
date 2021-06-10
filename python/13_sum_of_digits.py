def find_sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        rem = number % 10
        digit_sum += rem
        number = int(number / 10)
    
    return digit_sum

print(find_sum_of_digits(135))
print(find_sum_of_digits(11119))
print(find_sum_of_digits(2552))