def count_number_len(number):
    count = 0
    while number > 0:
        count += 1
        number = int(number / 10)
    return count

def is_armstrong(number):
    num = number
    number_length = count_number_len(number)
    sum = 0
    while num  > 0:
        sum += (num % 10) ** number_length
        num = num // 10
    return number == sum

def armstrong_in_range(lower, upper):
    armstrong_numbers = list()
    for number in range(lower, upper+1):
        if is_armstrong(number):
            armstrong_numbers.append(number)
    return armstrong_numbers

lower = 10
upper = 5000
armstrongs = armstrong_in_range(lower, upper)
for number in armstrongs:
    print(number)
