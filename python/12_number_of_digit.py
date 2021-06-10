def find_number_of_digit(number):
    count = 0
    
    while number > 0:
        number = int(number / 10)
        count += 1
    return count

print(find_number_of_digit(999))
print(find_number_of_digit(12))
print(find_number_of_digit(10002))