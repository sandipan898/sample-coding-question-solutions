def find_in_range_sun(lower, upper):
    sum = 0
    for i in range(lower, upper+1):
        sum += i
    return sum

print(find_in_range_sun(1, 10))
