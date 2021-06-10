def find_factorial(number):
    assert number >= 0 and number == int(number), "Enter an Non-negative whole Number"
    if number in [0, 1]:
        return 1
    return number*find_factorial(number-1)

print(find_factorial(5))
print(find_factorial(7))