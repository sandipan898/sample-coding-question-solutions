def find_natural_number_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    
    return sum

print(find_natural_number_sum([1, 2, 3, 4, 5, 6, 7]))
print(find_natural_number_sum(range(1, 11)))